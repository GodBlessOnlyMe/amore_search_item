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

    def _set_client(self):
        if not hasattr(self, 'client'):
            self.client = Es(self.config.get("host"))

    def get_client(self):
        if not hasattr(self, 'client'):
            self._set_client()
        return self.client

    def _set_helper(self):
        if not hasattr(self, 'client'):
            self._set_client()
        if not hasattr(self, 'helper'):
            self.helper = helpers

    def get_helper(self):
        if not hasattr(self, 'helper'):
            self._set_helper()
        return self.helper
