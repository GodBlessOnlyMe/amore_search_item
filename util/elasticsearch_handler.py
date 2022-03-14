from pathlib import Path

from elasticsearch import Elasticsearch as Es
from elasticsearch import helpers

from .config import get_config

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
ELASTICSEARCH_DIR = DATA_DIR / "elasticsearch"
TEMPLATES_DIR = ELASTICSEARCH_DIR / "templates"


class Elasticsearch:
    config = get_config('elasticsearch')
    client = Es(config.get("host"))
    helper = helpers

    def get_client(self):
        return self.client

    def get_helper(self):
        return self.helper
