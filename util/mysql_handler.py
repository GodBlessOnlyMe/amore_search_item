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

    def __init__(self, cursor_class=None):
        self.conn = None
        self.cursor = None
        self.cursor_class = cursor_class

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
        if not self.conn:
            self._set_conn()
        return self.conn

    def set_cursor(self):
        if not self.conn:
            self._set_conn()

        if self.cursor_class:
            self.cursor = self.conn.cursor(self.cursor_class)
        else:
            self.cursor = self.conn.cursor()

    def get_cursor(self):
        if not self.cursor:
            self.set_cursor()
        return self.cursor

    def close_cursor(self):
        if not self.cursor:
            self.cursor.close()

    def close_conn(self):
        if not self.conn:
            self.conn.close()
