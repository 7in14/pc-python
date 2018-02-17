import pytest

from app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client

def test_dummy(client):
    response = client.get('/index')
    assert b'Dummy app' in response.data