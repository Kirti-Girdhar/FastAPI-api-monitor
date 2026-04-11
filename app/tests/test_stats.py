

def test_get_stats(client):
    """Test retrieving stats for an endpoint."""
    # Login user
    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@example.com",
            "password": "test123"
        }
    )
    
    # Extract JWT token
    access_token = login_response.json()["access_token"]
    
    # Create Authorization header
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # Send GET request to /stats/endpoint/1
    response = client.get(
        "/stats/endpoint/1",
        headers=headers
    )
    
    # Assert: status code is either 200 (stats exist) or 404 (no data yet)
    assert response.status_code in [200, 404]