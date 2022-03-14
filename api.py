"""
api for searching products by keyword
"""

from flask import Flask, request

from src.service.search import Search

app = Flask(__name__)
search_service = Search()


@app.route('/', methods=['GET'])
def root():
    return "Hello Amore Pacific"


@app.route('/product/search/', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    result = search_service.product_search_by_keyword(keyword)
    return result


if __name__ == "__main__":
    app.run(debug=True)
