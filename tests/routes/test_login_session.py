from flask import session
    
def test_login_view(client):
    with client:
        response = client.post('/login',data={"username":"test@gmail.com","password":"test"})
        assert session['_user_id'] == 1