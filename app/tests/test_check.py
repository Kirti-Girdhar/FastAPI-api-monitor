import pytest
from unittest.mock import AsyncMock, MagicMock

from app.services.monitoring_service import check_endpoint


@pytest.mark.asyncio
async def test_check_endpoint_success(mocker):
    """Test successful endpoint check."""
    endpoint = MagicMock()
    endpoint.id = 1
    endpoint.url = "https://example.com"
    endpoint.method = "GET"

    # Mock database session
    db = MagicMock()

    # Mock HTTP response
    mock_response = MagicMock()
    mock_response.status_code = 200

    mock_request = AsyncMock(return_value=mock_response)

    # Mock the httpx.AsyncClient.request method
    mocker.patch(
        "app.services.monitoring_service.httpx.AsyncClient.request",
        mock_request
    )

    result = await check_endpoint(endpoint, db)
    
    assert result is not None
    assert result.status_code == 200
    assert result.success is True