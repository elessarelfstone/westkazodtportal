import cx_Oracle
import psycopg2
from configparser import ConfigParser


class DbMigration:
    def __init__(self, settings, section):
        parser = ConfigParser()
        parser.read(settings)
        _conn_settings = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                _conn_settings[param[0]] = param[1]
        else:
            raise Exception('Секция отсутсвует')
        self._conn_settings = _conn_settings


class DbOracle(DbMigration):
    def __init__(self, settings, section):
        super(DbOracle, self).__init__(settings, section)
        self._dsn = cx_Oracle.makedsn(self._conn_settings["host"], self._conn_settings["port"], self._conn_settings["sid"])
        self._conn = cx_Oracle.connect(self._conn_settings["user"], self._conn_settings["password"], self._dsn)

    def get_rows(self, sql):
        try:
            res = []
            curs = self._conn.cursor()
            curs.execute(sql)
            colnames = [desc[0] for desc in curs.description]
            for row in curs.fetchall():
                rw = {}
                for name, value in zip(colnames, row):
                    rw[name] = value
                res.append(rw)
            return res
        finally:
            self._conn.close()

    def get_rows_as_tuple(self, sql):
        try:
            res = []
            curs = self._conn.cursor()
            curs.execute(sql)
            for row in curs.fetchall():
                res.append(row)
            return res
        finally:
            self._conn.close()


class DbPostgreSQL(DbMigration):
    def __init__(self, settings, section):
        super(DbPostgreSQL, self).__init__(settings, section)
        self._conn_string = " ".join(["%s=%s" % (k, v) for k, v in self._conn_settings.items()])
        #print(self._conn_string)
        self._conn = psycopg2.connect(self._conn_string)

    def get_version_db(self):
        try:
            cur = self._conn.cursor()
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            return db_version
        finally:
            self._conn.close()

    def insert_rows(self, sql, rows):
        try:
            cur = self._conn.cursor()
            cur.executemany(sql, rows)
            self._conn.commit()
            cur.close()
        finally:
            self._conn.close()
