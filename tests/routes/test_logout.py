def test_login_view(client):
    #login first
    response = client.post('/login',data={"username":"test@gmail.com","password":"test"})
    
    # then logout
    response = client.post('/logout',follow_redirects=True)
    
    #check if redirect to login page
    assert response.request.path  == "/login"