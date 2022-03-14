# Search products by keyword

## Products
1. Case 1 데이터 Mapping Template
* ./data/elasticsearch/templates/product_index_template.json
2. Case 2 데이터 수집/정제/적재
* ./create_product_index_in_es_using_template.py
3. Case 3 상품 쿼리 작성
* ./src/service/search.py
4. Case 4 상품 검색 API
* ./api.py

## Usage
```shell
# docker container 실행
python3 run_containers.py --type={mysql, elasticsearch, kibana, all}
  
# sql 파일로 mysql dummy 데이터 dump
python3 sql_to_mysql.py  

# create both index template and index in elasticsearch
python3 create_product_index_in_es_using_template.py 

# mysql 데이터를 elasticsearch bulk dump
python3 mysql_to_es.py  

# 상품검색 API(flask)를 실행
python3 api.py

# 키워드로 상품 검색
curl -X GET http://localhost:5000/product/search/?keyword=손크림
```
## Environment
```text
Ubuntu 20.04.3 LTS
Docker 4.1.1
Python 3.8.10
Elasticsearch 7.5.1
Kibana 7.5.1
MySQL 8.0.20
```

## Libraries
```text
PyMySQL==1.0.2
docker~=5.0.3
PyYAML~=5.3.1
elasticsearch~=7.5.1
Flask~=2.0.3
tqdm~=4.63.0
requests~=2.26.0
```

## TODO
- ~~주석 적기~~
- ~~프로젝트 구조 작성~~
- ~~개발환경 작성~~
- ~~라이브러리 작성~~


