class SearchResponse:

    def response_from_es_result_by_keyword(self, keyword, hits_from_es):
        response = {
            "query_keyword": keyword,
            "search_result": [
                {
                    "rank": i,
                    "score": hits_from_es[i].get("_score"),
                    **hits_from_es[i].get("_source")
                }
                for i, d in enumerate(hits_from_es)
            ]

        }
        return response
