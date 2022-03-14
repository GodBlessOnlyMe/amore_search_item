"""
create elasticsearch index template and then create product index
"""

import os

import requests

from util.elasticsearch_handler import Elasticsearch
from util.elasticsearch_handler import TEMPLATES_DIR

es = Elasticsearch()


def main():
    template_name = "product_template"
    template_file_name = "product_index_template.json"
    index_name = "product"

    with open(os.path.join(TEMPLATES_DIR, template_file_name), "r") as f:
        template = f.read()
        create_index_template(template_name, template)
        create_index(index_name)


def create_index_template(template_name, template):
    """create elasticsearch index template by template name and template
    :param template_name: the name for created template
    :type template_name: str
    :param template: json string
    :type template: str
    """
    uri = es.config.get("host") + f"/_template/{template_name}"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    resp = requests.put(uri, data=template.encode('utf-8'), headers=headers)
    print(resp, resp.text)


def create_index(index_name):
    """create elasticsearch index by index name
    :param index_name: the name for created index
    :type index_name: str
    """
    uri = es.config.get("host") + f"/{index_name}"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    resp = requests.put(uri, headers=headers)
    print(resp, resp.text)


if __name__ == '__main__':
    main()
