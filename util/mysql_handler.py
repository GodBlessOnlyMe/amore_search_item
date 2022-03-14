from pathlib import Path

import pymysql

from .config import get_config

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
MYSQL_DIR = DATA_DIR / "mysql"
SQL_DIR = MYSQL_DIR / "sqls"
DUMMY_DIR = SQL_DIR / "dummy"


class Mysql(object):
    config = get_config('mysql')

    def _set_conn(self):
        conn = pymysql.connect(
            host=self.config.get("host"),
            port=int(self.config.get("port")),
            user=self.config.get("user"),
            password=self.config.get("password"),
            db=self.config.get("database"),
            charset='utf8'
        )
        self.conn = conn

    def get_conn(self):
        if not hasattr(self, 'conn'):
            self._set_conn()
        return self.conn

    def _set_cursor(self):
        if not hasattr(self, 'conn'):
            self._set_conn()
        self.cursor = self.conn.cursor()

    def get_cursor(self):
        if not hasattr(self, 'cursor'):
            self._set_cursor()
        return self.cursor

    def close_cursor(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()

    def close_conn(self):
        if hasattr(self, 'conn'):
            self.conn.close()
