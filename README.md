# 아모레퍼시픽 과제

## 산출물
1. Case 1 데이터 Mapping Template
* ./data/elasticsearch/templates/product_index_template.json
2. Case 2 데이터 수집/정제/적재
* ./create_product_index_in_es_using_template.py
3. Case 3 상품 쿼리 작성
* ./src/service/search.py
4. Case 4 상품 검색 API
* ./api.py

## 사용법
```shell
python3 main.py --type=mysql  # mysql docker container 실행
python3 dump_sql_to_mysql.py  # sql 파일로 mysql dummy 데이터 dump
python3 main.py --type=elasticsearch  # elasticsearch docker container 실행 및 nori_tokenizer 설치
python3 main.py --type=kibana  # kibana docker container 실행
python3 dump_from_mysql_to_es.py  # mysql 데이터를 elasticsearch bulk dump
python3 api.py  # 상품검색 API(flask)를 실행
```

## 프로젝트 구조

## 개발 환경

## 라이브러리


## TODO
- ~~주석 적기~~
- type hint
- 프로젝트 구조 작성
- 개발환경 작성
- 라이브러리 작성


