import pytest
from cp_api.run import predict

@pytest.mark.parametrize('inp, res', [
    (1, 'OK'),
    (2, 'HZ'),
    (0, 'NO'),
    (-10, 'HZ')
])
def test_01(inp, res):
    assert predict(inp) == res

class TestRun:
    def test_02(self):
        print(f'test_02_started')

    def test_03(self):
        print(f'test_03_started')



