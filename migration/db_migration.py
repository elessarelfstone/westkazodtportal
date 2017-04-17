import cx_Oracle
import psycopg2
from configparser import ConfigParser
import logging

class DbMigration2:

    def __init__(self, settings):

        """
         получение параметров подключений у обеих баз из ini файла
         установка подключений
         установка праметров логирования

        """

        # настройка логирования
        self._application_name = "Telecom_Storage"
        self.logger = logging.getLogger(self._application_name)
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

        file_handler = logging.FileHandler('storage.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.WARNING)
        console.setFormatter(formatter)

        self.logger.addHandler(console)
        self.logger.addHandler(file_handler)

        self.conditions = ()

        try:
            # получение настроек из ini файлов
            parser = ConfigParser()
            parser.read(settings)
            _conn_oracle_sett = {}
            _conn_postgres_sett = {}
            if parser.has_section('oracle') and parser.has_section('postgres'):
                params = parser.items('oracle')
                for param in params:
                    _conn_oracle_sett[param[0]] = param[1]
                params = parser.items('postgres')
                for param in params:
                    _conn_postgres_sett[param[0]] = param[1]
            else:
                raise Exception('Секции отсуствуют')
            self._conn_oracle_sett = _conn_oracle_sett
            self._conn_postgres_sett = _conn_postgres_sett
            # создание подключения к базе oracle

            self._dsn = cx_Oracle.makedsn(self._conn_oracle_sett["host"], self._conn_oracle_sett["port"],
                                      self._conn_oracle_sett["sid"])
            self._oracle_conn = cx_Oracle.connect(self._conn_oracle_sett["user"], self._conn_oracle_sett["password"],
                                              self._dsn)

            self._conn_postgres_string = " ".join(["%s=%s" % (k, v) for k, v in self._conn_postgres_sett.items()])
            # print(self._conn_string)
            self._postgres_conn = psycopg2.connect(self._conn_postgres_string)
        except Exception as e:
            self.logger.exception(e)

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
                #rcnt = pg_cur.rowcount
                self.logger.info('В таблицу ' + tbl + ' всталено ' + str(pg_cur.rowcount) + ' записей. ')

            self._postgres_conn.commit()

            self.logger.warning('Процедура экспорта лицевых счетов абонетов завершена')
        except Exception as e:
            self.logger.exception(e)
        finally:
            self._oracle_conn.close()
            self._postgres_conn.close()


    def get_prepared_script(self, template):
        pass

