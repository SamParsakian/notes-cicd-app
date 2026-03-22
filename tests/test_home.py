"""Basic checks for the home page."""


def test_home_returns_success(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_expected_text(client):
    response = client.get("/")
    assert b"notes-cicd-app" in response.data
