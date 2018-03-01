import pytest

from app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client

def test_ping(client):
    response = client.get('/ping')
    assert b'pong' in response.data

def test_file(client):
    response = client.get('/file')
    assert b'7in14 python' in response.data

def test_crime(client):
    response = client.get('/raleigh/crime?query=lcr=51C&district=SOUTHWEST')
    assert b'district' in response.data