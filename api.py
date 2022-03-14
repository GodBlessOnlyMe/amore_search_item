"""
api for searching products by keyword
"""

from flask import Flask, request

from src.service.search import Search
from data.search.search_response import SearchResponse

app = Flask(__name__)
search_service = Search()
search_response = SearchResponse()


@app.route('/', methods=['GET'])
def root():
    return "Hello Amore Pacific"


@app.route('/product/search/', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    result = search_service.product_search_by_keyword(keyword)
    hits = result.get('hits').get('hits')
    response = search_response.response_from_es_result_by_keyword(keyword, hits)
    return response


if __name__ == "__main__":
    app.run(debug=True)
