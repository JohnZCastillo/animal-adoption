from flask import session
    
def test_login_view(client):
    with client:
        response = client.post('/animal/type',data={"name":"cat"},follow_redirects=True)
        
        assert response.request.path == '/animal/register'
        