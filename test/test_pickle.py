from pytest import fixture
from pickle import dumps, loads


class Picklable:
    def __init__(self, y, x=None, **kwargs):
        self.x = x
        self.y = y


class TestPicklable:
    @fixture
    def data_args(self):
        return {
            'y': 2,
            'x': 1
        }

    @fixture
    def picklable(self, data_args):
        return Picklable(**data_args)

    def test_works(self, picklable, data_args):
        vlasic = dumps(picklable)
        back = loads(vlasic)
        print(back.x)
        assert back.x == 1

    def test_write(self, picklable):
        with open('/tmp/asdf', 'wb+') as ptr:
            ptr.write(dumps(picklable))

