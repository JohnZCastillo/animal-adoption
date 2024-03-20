def test_login_view(client):
    response = client.get('/login')
    assert response.status_code  == 200