from makeup import delegate as obv


def load():
    """
    should always accept no arguments?
    :return:
    """
    return open("test/fixtures/module_level.tsv")


class TestLoad:
    def test_this(self):
        """delegate to this file (see above)"""
        data = obv.load(__name__)
        iou = data.read()
        assert iou[:2] == 'id'

    def test_tsv_dataset(self):
        dataset = 'test/fixtures/data.tsv'
        data = obv.load(__name__, dataset)
        iou = data.read()
        assert iou[:2] == 'id'

    def test_http(self):
        pass
