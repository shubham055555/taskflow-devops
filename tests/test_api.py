import pytest
from app import app, db, Task


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.drop_all()
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={
            "title": "Test Task",
            "description": "Testing TaskFlow",
            "status": "pending"
        }
    )

    assert response.status_code == 201
    assert response.json["title"] == "Test Task"


def test_get_tasks(client):
    client.post(
        "/api/tasks",
        json={
            "title": "Test Task",
            "description": "Testing",
            "status": "pending"
        }
    )

    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert len(response.json) == 1


def test_update_task(client):
    create_response = client.post(
        "/api/tasks",
        json={
            "title": "Old Task",
            "description": "Old description",
            "status": "pending"
        }
    )

    task_id = create_response.json["id"]

    response = client.put(
        f"/api/tasks/{task_id}",
        json={
            "title": "Updated Task",
            "description": "Updated description",
            "status": "completed"
        }
    )

    assert response.status_code == 200
    assert response.json["title"] == "Updated Task"
    assert response.json["status"] == "completed"


def test_delete_task(client):
    create_response = client.post(
        "/api/tasks",
        json={
            "title": "Delete Me",
            "description": "Temporary task",
            "status": "pending"
        }
    )

    task_id = create_response.json["id"]

    response = client.delete(f"/api/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json["message"] == "Task deleted successfully"
