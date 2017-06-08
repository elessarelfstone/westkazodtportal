import db

class DbMigration(db.DB):
    def __init__(self, settings, conn_mode):
        super(DbMigration, self).__init__(settings, conn_mode)

    def export_abonents(self):
        """ Производит заливку лицевых счетов из БИТТл в таблицы хранилища """
        try:
            # получаем лицевые счета абонентов из БИТТл
            self.logger.warning('Старт процедуры экспорта лицевых счетов абонентов')
            or_cur = self._oracle_conn.cursor()
            sql = "select id from db.abonent"
            or_cur.execute(sql)

            # abns = [ abn[0] for abn in or_cur.fetchall()]
            abns = or_cur.fetchall()
            self.logger.info('Выбрано лицевых счетов в количестве '+ str(len(abns)))
            pg_cur = self._postgres_conn.cursor()
            # получаем список таблиц в которые будем заливать лицевые счета абонентов с БИТТл
            sql = "select table_name from storage.data_type dt where dt.base = %s"
            pg_cur.execute(sql, ("ABN", ))
            tables = [tp[0] for tp in pg_cur.fetchall()]

            #  обнуляем эти таблицы и заливаем туда лицевые счета
            for tbl in tables:
                sql = 'truncate table '+ tbl
                pg_cur.execute(sql)
                self.logger.info('Таблица ' + tbl + ' обнулена')
                sql = "insert into "+tbl+"(abonent_id) values(%s)"
                pg_cur.executemany(sql, abns)
                self.logger.info('В таблицу ' + tbl + ' всталено ' + str(pg_cur.rowcount) + ' записей. ')
            self._postgres_conn.commit()
            self.logger.warning('Процедура экспорта лицевых счетов абонетов завершена')
        except Exception as e:
            self.logger.exception(e)

    def fill_abn_column(self, sql, column, dest_table):
        """ заливка данных одной колонки """
        try:
            self.logger.warning('Старт заливки данных столбца ' + column + ' в таблице '+ dest_table)
            or_cur = self._oracle_conn.cursor()
            or_cur.execute(sql)
            data = or_cur.fetchall()
            # меняем порядок колонок для удобной подстановки в скрипт заливки
            data = [dt[::-1] for dt in data]
            # формируем сам скрипт заливки(обновления)
            fill_sql = "update " + dest_table + " t set " + column + " = %s where t.abonent_id = %s"
            pg_cur = self._postgres_conn.cursor()
            pg_cur.executemany(fill_sql, data)
            self._postgres_conn.commit()
            self.logger.warning('Заливка столбца данных столбца ' + column + ' в таблице ' + dest_table + ' окончена')
        except Exception as e:
            self.logger.exception(e)

    def fill_all_abn_columns(self):
        """ заливка всех колонок """
        try:
            # получаем скрипт выбоки всех колонок для заливки из файла
            # f = open('sql//pg_all_abn_columns.sql')
            # lines = f.readlines()
            # sql = ''.join(lines)
            sql = "select * from storage.view_storage_columns"
            pg_cur = self._postgres_conn.cursor()
            pg_cur.execute(sql)
            clmnames = [desc[0] for desc in pg_cur.description]
            rows = []
            # преобразуем полученный список с колонками в список словарей для удобного вызова функции fill_abn_column
            for row in pg_cur.fetchall():
                rw = {}
                for name, value in zip(clmnames, row):
                    rw[name] = value
                rows.append(rw)
            # итерируем по колонкам и заливаем их.
            for row in rows:
                self.fill_abn_column(row["script"], row["column_name"], row["table_name"])
        except Exception as e:
            self.logger.exception(e)

    def main(self):
        "Полный цикл работ. Обнуление, заливка абонентов, заливка данных"
        try:
            self.export_abonents()
            self.fill_all_abn_columns()
        finally:
            self._oracle_conn.close()
            self._postgres_conn.close()