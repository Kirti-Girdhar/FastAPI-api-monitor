import pytest
from unittest.mock import patch

# from app.tests.conftest import client

@pytest.mark.asyncio
@patch("app.services.monitoring_service.httpx.AsyncClient.get")
async def test_check_endpoint_success(mock_get, client):
    # Mock a successful response
    mock_get.return_value.status_code = 200
    response = client.get("check/run")

    assert response.status_code == 200