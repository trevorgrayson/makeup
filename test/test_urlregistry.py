from urllib import request
from makeup.urlregistry.sqlite import SQLiteHandler
from pickle import load
# TODO Deserializer

opener = request.build_opener(SQLiteHandler())
request.install_opener(opener)


class TestUrlRegistry:
    def test_sql_read(self):
        response = request.urlopen(
            'sql:./test/fixtures/sql/select.sql'
        )
        doc = load(response)
        assert doc[0][0] == 1
        assert doc[0][1] == 'angus'

    def test_file_read(self):
        response = request.urlopen(
            'file:./test/fixtures/data.tsv'
        )
        assert response.read().decode('utf-8')\
            .startswith("id\tname\temail\n1\ttrevor")

    # def test_http_read(self):
    #     response = request.urlopen(
    #        'http://trevorgrayson.com'
    #     )
    #     doc = response.read()

    # def test_https_read(self):
    #     response = request.urlopen(
    #         'https://trevorgrayson.com'
    #     )
    #     doc = response.read()

    # sql+snow:./sql/whatever.sql
