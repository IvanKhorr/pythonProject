import pytest

@pytest.fixture(autouse=True)
def auto_fixt():
    print('\nAtoused fixture')