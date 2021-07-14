from urllib import request
from makeup.urlregistry.sqlite import SQLiteHandler
from pickle import load

opener = request.build_opener(SQLiteHandler())
request.install_opener(opener)


class TestSQLitehandler:
    def test_sql_read(self):
        response = request.urlopen(
            'sql:./test/fixtures/sql/select.sql'
        )
        doc = load(response)
        assert doc[0][0] == 1
        assert doc[0][1] == 'angus'
