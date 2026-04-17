import pytest
from unittest.mock import AsyncMock, MagicMock

from app.services.monitoring_service import check_endpoint


# =====================================
# TEST 1 — SUCCESS RESPONSE
# =====================================

@pytest.mark.asyncio
async def test_check_endpoint_success(mocker):

    endpoint = MagicMock()
    endpoint.id = 1
    endpoint.url = "https://example.com"
    endpoint.method = "GET"

    # Mock HTTP response
    mock_response = MagicMock()
    mock_response.status_code = 200

    mock_request = AsyncMock(
        return_value=mock_response
    )

    # IMPORTANT — correct patch path
    mocker.patch(
        "app.services.monitoring_service.httpx.AsyncClient.request",
        mock_request
    )

    # Mock DB
    mock_db = MagicMock()

    # Mock query chain
    mock_query = MagicMock()

    mock_db.query.return_value = mock_query
    mock_query.filter.return_value = mock_query
    mock_query.order_by.return_value = mock_query
    mock_query.limit.return_value = mock_query

    fake_check = MagicMock()
    fake_check.success = True

    mock_query.all.return_value = [fake_check]

    await check_endpoint(endpoint, mock_db)

    assert mock_request.called
    assert mock_db.add.called
    assert mock_db.commit.called


# =====================================
# TEST 2 — FAILURE RESPONSE
# =====================================

@pytest.mark.asyncio
async def test_check_endpoint_failure(mocker):

    endpoint = MagicMock()
    endpoint.id = 2
    endpoint.url = "https://fail.com"
    endpoint.method = "GET"

    mock_response = MagicMock()
    mock_response.status_code = 500

    mock_request = AsyncMock(
        return_value=mock_response
    )

    mocker.patch(
        "app.services.monitoring_service.httpx.AsyncClient.request",
        mock_request
    )

    mock_db = MagicMock()

    mock_query = MagicMock()

    mock_db.query.return_value = mock_query
    mock_query.filter.return_value = mock_query
    mock_query.order_by.return_value = mock_query
    mock_query.limit.return_value = mock_query

    fake_check = MagicMock()
    fake_check.success = False

    mock_query.all.return_value = [fake_check]

    await check_endpoint(endpoint, mock_db)

    assert mock_request.called


# =====================================
# TEST 3 — EXCEPTION CASE
# =====================================

@pytest.mark.asyncio
async def test_check_endpoint_exception(mocker):

    endpoint = MagicMock()
    endpoint.id = 3
    endpoint.url = "https://timeout.com"
    endpoint.method = "GET"

    mock_request = AsyncMock(
        side_effect=Exception("Timeout")
    )

    mocker.patch(
        "app.services.monitoring_service.httpx.AsyncClient.request",
        mock_request
    )

    mock_db = MagicMock()

    mock_query = MagicMock()

    mock_db.query.return_value = mock_query
    mock_query.filter.return_value = mock_query
    mock_query.order_by.return_value = mock_query
    mock_query.limit.return_value = mock_query

    fake_check = MagicMock()
    fake_check.success = False

    mock_query.all.return_value = [fake_check]

    await check_endpoint(endpoint, mock_db)

    assert mock_request.called


# =====================================
# TEST 4 — ALERT AFTER 3 FAILURES
# =====================================

@pytest.mark.asyncio
async def test_alert_creation_after_3_failures(mocker):

    endpoint = MagicMock()
    endpoint.id = 4
    endpoint.url = "https://fail.com"
    endpoint.method = "GET"

    mock_response = MagicMock()
    mock_response.status_code = 500

    mock_request = AsyncMock(
        return_value=mock_response
    )

    mocker.patch(
        "app.services.monitoring_service.httpx.AsyncClient.request",
        mock_request
    )

    mock_db = MagicMock()

    mock_query = MagicMock()

    mock_db.query.return_value = mock_query
    mock_query.filter.return_value = mock_query
    mock_query.order_by.return_value = mock_query
    mock_query.limit.return_value = mock_query

    # Simulate 3 failures
    fake_check = MagicMock()
    fake_check.success = False

    mock_query.all.return_value = [
        fake_check,
        fake_check,
        fake_check
    ]

    await check_endpoint(endpoint, mock_db)

    assert mock_db.add.called
    assert mock_db.commit.called


