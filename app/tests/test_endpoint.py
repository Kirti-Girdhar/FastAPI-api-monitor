
def test_create_endpoint(client):
    """Test creating an endpoint with authentication."""
    # Login first
    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@example.com",
            "password": "test123"
        }
    )
    
    # Extract access token
    access_token = login_response.json()["access_token"]
    
    # Create Authorization header
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # Send POST request to create endpoint
    response = client.post(
        "/endpoints/",
        json={
            "name": "Test Endpoint",
            "url": "https://example.com",
            "method": "GET",
            "check_interval": 60
        },
        headers=headers
    )
    
    # Assert status code
    assert response.status_code in [200, 201]
    
    # Extract response JSON
    data = response.json()
    
    # Assert response contains required fields
    assert "id" in data
    assert "url" in data



def test_get_endpoints(client):
    """Test retrieving list of endpoints with authentication."""
    # Login user
    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@example.com",
            "password": "test123"
        }
    )
    
    # Extract token
    access_token = login_response.json()["access_token"]
    
    # Create Authorization header
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # Send GET request to /endpoints/
    response = client.get(
        "/endpoints/",
        headers=headers
    )
    
    # Assert status code == 200
    assert response.status_code == 200
    
    # Assert response JSON contains list of endpoints
    data = response.json()
    assert isinstance(data, list)


def test_unauthorized_access(client):
    """Test that accessing protected endpoint without Authorization header returns 401."""
    # Send GET request to /endpoints/ WITHOUT Authorization header
    response = client.get("/endpoints/")
    
    # Assert status code == 401
    assert response.status_code == 401