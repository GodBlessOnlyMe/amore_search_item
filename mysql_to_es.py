"""
dump data from mysql to elasticsearch
"""

import os

import pymysql.cursors

from util.mysql_handler import Mysql
from util.mysql_handler import SQL_DIR
from util.elasticsearch_handler import Elasticsearch

es_client = Elasticsearch.client
es_helper = Elasticsearch.helper

mysql = Mysql(cursor_class=pymysql.cursors.DictCursor)
mysql_cursor = mysql.get_cursor()


def main():
    # Select products joined category from mysql
    sql_file_name = "select_product_joined_category.sql"
    with open(os.path.join(SQL_DIR, sql_file_name), "r") as sql_file:
        sql = sql_file.read()
        mysql_cursor.execute(sql)
        products = mysql_cursor.fetchall()

    mysql.close_cursor()
    mysql.close_conn()

    # Convert products into document-style
    products = [
        {
            "_index": "product",
            "_id": idx,
            "_source": val
        }
        for idx, val in enumerate(products)
    ]

    # Bulk insert into es
    es_helper.bulk(es_client, products)


if __name__ == '__main__':
    main()
