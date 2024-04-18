from flask import session
    
def test_login_view(client):
    with client:
        response = client.get('/animal/register')
        assert response.status_code == 200