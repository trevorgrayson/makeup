from makeup import delegate as obv


def load():
    """
    should always accept no arguments?
    :return:
    """
    return open("test/fixtures/module_level.tsv")


def features(df):
    return df


class TestFeatures:
    def test_features(self):
        """
        delegate to this file (see above)
        looking up by module name
        """
        feats = obv.features(__name__)
        assert feats.read()[:2] == 'id'