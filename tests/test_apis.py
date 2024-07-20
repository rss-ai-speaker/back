import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()

    return client


def test_summarize(client):
    response = client.get('/api/summarize')
    assert len(response.text) > 100
