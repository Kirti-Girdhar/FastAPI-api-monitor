
def test_user_registration(client):
    """Test user registration endpoint."""
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "test123"
        }
    )
    # Accept 200, 201 for successful registration, or 400 if user already exists
    assert response.status_code in [200, 201, 400]


def test_user_login(client):
    """Test user login endpoint."""
    response = client.post(
        "/auth/login",
        data={
            "username": "test@example.com",
            "password": "test123"
        }
    )
    assert response.status_code == 200
    
    data = response.json()
    assert "access_token" in data



def test_invalid_login(client):
    """Test that invalid credentials are rejected."""
    # Send POST request to /auth/login with wrong credentials
    response = client.post(
        "/auth/login",
        data={
            "username": "wrong@example.com",
            "password": "wrongpass"
        }
    )
    
    # Assert status code == 401 or 400
    assert response.status_code in [401, 400]