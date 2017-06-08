import cx_Oracle
import psycopg2
from configparser import ConfigParser
import logging

class DB:
    """Базовый класс для работы с обеими базами данных"""
    def __init__(self, settings, conn_mode):

        """
         получение параметров подключений у обеих баз из ini файла
         установка подключений
         установка праметров логирования

        """

        self._isOracleEnabled = 'oracle'
        self._isPostgresEnabled = 'postgres'

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
                raise Exception('Секции отсутсвуют')
            self._conn_oracle_sett = _conn_oracle_sett
            self._conn_postgres_sett = _conn_postgres_sett
            # создание подключения к базе oracle
            if self._isOracleEnabled in conn_mode:
                self._dsn = cx_Oracle.makedsn(self._conn_oracle_sett["host"], self._conn_oracle_sett["port"],
                                          self._conn_oracle_sett["sid"])
                self._oracle_conn = cx_Oracle.connect(self._conn_oracle_sett["user"], self._conn_oracle_sett["password"],
                                                  self._dsn)
            if self._isPostgresEnabled in conn_mode:
                self._conn_postgres_string = " ".join(["%s=%s" % (k, v) for k, v in self._conn_postgres_sett.items()])
                self._postgres_conn = psycopg2.connect(self._conn_postgres_string)
        except Exception as e:
            self.logger.exception(e)



