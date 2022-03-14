from util.elasticsearch_handler import Elasticsearch


class Search:
    """
    검색 서비스를 관리한다.
    """
    es = Elasticsearch()
    es_client = es.get_client()
    es_config = Elasticsearch.config
    boost_info = es_config.get("boost_info")

    def product_search_by_keyword(self, keyword, size=100):
        """search product-index documents by keyword
        :param keyword: query keyword
        :type keyword: str
        :param size: the number of search result
        :type size: int
        """

        body = {
            "size": size,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "product_name": {
                                    "query": keyword
                                }
                            }
                        }
                    ],
                    "should": [
                        {
                            "match": {
                                "category_depth1_name": {
                                    "query": self.boost_info.get('category_depth1_name').get('query'),
                                    "boost": self.boost_info.get('category_depth1_name').get('boost')
                                }
                            }
                        }
                    ]
                }
            }
        }
        result = self.es_client.search(index="product", body=body)
        return result
