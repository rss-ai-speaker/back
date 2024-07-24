import json

import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()

    return client


def test_summarize(client):
    response = client.get('/api/summarize?id=https://www.reddit.com/r/Python/comments/wzswh9/is_flask_even_being_used_nowdays/.rss')
    assert len(response.text) > 100


def test_post_summarize(client):
    data = {
        "link":"https://www.reddit.com/r/reinforcementlearning/.rss"
    }
    response = client.post('/api/summarize',data=json.dumps(data),
                headers={"Content-Type": "application/json"})
    assert response.status_code == 201


def test_get_content(client):
    # default id is 3e962c3a-1735-4d96-90bb-17439d8c01e6
    response = client.get('/api/list/3e962c3a-1735-4d96-90bb-17439d8c01e6')

    assert response.status_code == 200 and response.data
    assert type(response.data) == bytes


def test_get_content_list(client):
    response = client.get('/api/list')

    assert response.status_code == 200 and response.data
    assert type(response.data) is bytes
