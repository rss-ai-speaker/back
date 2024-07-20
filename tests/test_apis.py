import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()

    return client


def test_summarize(client):
    response = client.post('/api/summarize', json={'id': '1'})
    assert response.status.find('200') or response.status.find('201')
