from makeup.url_cache import cache_by_url

CACHE_PATH = 'file:./test/fixtures'


def cache_miss():
    return [1, 2, 3]


def precached():
    return [4, 5, 6]
    raise Exception("this test failed!")


class TestUrlCache:
    def test_cache_by_url(self):
        result = cache_by_url(cache_miss, CACHE_PATH)
        assert result == cache_miss()

    def test_cache_by_url_precached(self):
        result = cache_by_url(precached, CACHE_PATH)
        assert result == [4, 5, 6]
