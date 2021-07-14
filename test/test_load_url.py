from makeup import run
from examples import load_file


class TestLoadUrl:
    def test_load_url(self):
        result = run(load_file, 'features')
        row = result[0]
        assert len(row) == 3
