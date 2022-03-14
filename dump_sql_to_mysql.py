"""
insert dummy data(sql) to mysql
"""
import os

from tqdm import tqdm

from util.mysql_handler import DUMMY_DIR
from util.mysql_handler import Mysql

mysql = Mysql()
conn = mysql.get_conn()


def dump_sql_to_mysql(sql_file_name):
    cursor = mysql.get_cursor()
    with open(os.path.join(DUMMY_DIR, sql_file_name)) as sql:
        sql_lines = sql.read().split(';')
        for sql_line in tqdm(sql_lines):
            if sql_line:
                cursor.execute(sql_line)
    conn.commit()


if __name__ == '__main__':
    sql_files = os.listdir(DUMMY_DIR)
    for sql_file in sql_files:
        dump_sql_to_mysql(sql_file)
