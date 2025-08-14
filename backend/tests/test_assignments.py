from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_assignments_empty():
    resp = client.get('/api/assignments')
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_create_assignment_and_get():
    payload = {
        "course_id": "cs101",
        "title": "Test Homework",
        "due_date": "2025-08-20T23:59:00"
    }
    resp = client.post('/api/assignments', json=payload)
    assert resp.status_code == 200 or resp.status_code == 201
    data = resp.json()
    assert data['title'] == payload['title']
    assert 'id' in data

    # now retrieve and ensure it appears
    all_resp = client.get('/api/assignments')
    assert all_resp.status_code == 200
    items = all_resp.json()
    assert any(item['id'] == data['id'] for item in items)
