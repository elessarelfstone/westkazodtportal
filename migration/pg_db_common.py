import db


class StorageApi(db.DB):
    def __init__(self, settings, conn_mode):
        super(StorageApi, self).__init__(settings, conn_mode)

    # TODO: построить дерево(граф)
    def get_abn_tree(self):
        """получаем данные по абонентам для дерева в gui"""
        try:
            sql = "select * from storage.view_storage_abn_tree"
            pg_cur = self._postgres_conn.cursor()
            pg_cur.execute(sql)
            clmnames = [desc[0] for desc in pg_cur.description]
            rows = []
            # преобразуем полученный список с колонками в список словарей
            for row in pg_cur.fetchall():
                rw = {}
                for name, value in zip(clmnames, row):
                    rw[name] = value
                rows.append(rw)
            return rows
        finally:
            pass


