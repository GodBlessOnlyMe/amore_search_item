"""
dump data from mysql to elasticsearch
"""

import os

from util.mysql_handler import Mysql
from util.mysql_handler import SQL_DIR
from util.elasticsearch_handler import Elasticsearch

es = Elasticsearch()
es_client = es.get_client()
es_helper = es.get_helper()

mysql = Mysql()
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
            "_source": {
                "product_no": val[0],
                "product_name": val[1],
                "product_price": val[2],
                "brand_name": val[3],
                "category_depth1_no": val[4],
                "category_depth1_name": val[5],
                "category_depth2_no": val[6],
                "category_depth2_name": val[7]
            }
        }
        for idx, val in enumerate(products)]

    # Bulk insert into es
    es_helper.bulk(es_client, products)


if __name__ == '__main__':
    main()
