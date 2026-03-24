def test_delete_note(client):
    client.post("/", data={"note": "test"})
    response = client.post("/delete/0")
    assert response.status_code == 302
