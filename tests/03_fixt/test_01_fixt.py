import pytest
from cp_api.run import predict

@pytest.fixture
def data_01(request):
    print('\nBegin in fixt')
    print(f'\nCall from {request.function.__name__} ')
    yield
    print('\nRolling back in fixt data_01 ')

@pytest.fixture
def print_hello():
    print('\nHello')

def test_data_01(data_01, print_hello):
    pass
    #assert data_01 ==1

def test_data_02(auto_fixt):
    pass




