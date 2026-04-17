import pytest
import httpx

from unittest.mock import AsyncMock, MagicMock

from app.services.monitoring_service import (
    check_endpoint,
    MAX_RETRIES
)

from app.models.endpoint import Endpoint


# Helper function to mock DB query chain
def mock_db_with_empty_checks(mocker):

    mock_db = MagicMock()

    # Mock query chain
    mock_query = MagicMock()

    mock_db.query.return_value = mock_query

    mock_query.filter.return_value = mock_query
    mock_query.order_by.return_value = mock_query
    mock_query.limit.return_value = mock_query

    # Important: return list here
    mock_query.all.return_value = []

    mock_query.first.return_value = None

    return mock_db


@pytest.mark.asyncio
async def test_retry_logic(mocker):

    endpoint = Endpoint(
        id=1,
        url="https://slow-site.com",
        method="GET"
    )

    # Always timeout
    mock_request = AsyncMock(
        side_effect=httpx.TimeoutException(
            "Timeout"
        )
    )

    mocker.patch(
        "httpx.AsyncClient.request",
        mock_request
    )

    mock_db = mock_db_with_empty_checks(mocker)

    await check_endpoint(
        endpoint,
        mock_db
    )

    # Should retry MAX_RETRIES times
    assert mock_request.call_count == MAX_RETRIES


@pytest.mark.asyncio
async def test_retry_success(mocker):

    endpoint = Endpoint(
        id=2,
        url="https://example.com",
        method="GET"
    )

    mock_response = mocker.Mock()
    mock_response.status_code = 200

    mock_request = AsyncMock(
        return_value=mock_response
    )

    mocker.patch(
        "httpx.AsyncClient.request",
        mock_request
    )

    mock_db = mock_db_with_empty_checks(mocker)

    await check_endpoint(
        endpoint,
        mock_db
    )

    # Should stop after first success
    assert mock_request.call_count == 1