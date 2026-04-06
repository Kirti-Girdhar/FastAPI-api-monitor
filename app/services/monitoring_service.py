import httpx
import time
import logging
from sqlalchemy.orm import Session

from app.models.check import Check
from app.models.alert import Alert

logger=logging.getLogger(__name__)


async def check_endpoint(endpoint, db: Session):

    start_time = time.time()

    success = False
    status_code = 0

    try:
        logger.info(f"Checking endpoint: {endpoint.url} using method {endpoint.method}")
        async with httpx.AsyncClient() as client:

            response = await client.request(
                method=endpoint.method,
                url=endpoint.url,
                timeout=5
            )

        status_code = response.status_code

        if status_code < 400:
            success = True
        
        # logger.info(f"Checked {endpoint.url} | Status: {status_code} | Success: {success}")

    except Exception as e:
        success = False
        status_code = 0 
        logger.error(f"Request failed for {endpoint.url} "
            f"Error: {str(e)}")
        
    response_time = time.time() - start_time
    logger.info(
        f"Checked {endpoint.url} | "
        f"Status: {status_code} | "
        f"Success: {success} | "
        f"Time: {response_time:.2f}s"
    )

    # Save result
    check = Check(
        endpoint_id=endpoint.id,
        status_code=status_code,
        response_time=response_time,
        success=success
    )

    db.add(check)
    db.commit()

    last_checks = (
    db.query(Check)
    .filter(Check.endpoint_id == endpoint.id)
    .order_by(Check.checked_at.desc())
    .limit(3)
    .all()
    )

    # Check if last 3 failed
    three_failures = (
        len(last_checks) == 3
        and all(not c.success for c in last_checks)
    )

    if three_failures:
        # Check if an unresolved alert already exists
        existing_alert = (
            db.query(Alert)
            .filter(Alert.endpoint_id == endpoint.id)
            .order_by(Alert.created_at.desc())
            .first()
        )

        if not existing_alert:
            alert = Alert(
                endpoint_id=endpoint.id,
                message="Endpoint failed 3 consecutive times"
            )

            db.add(alert)
            db.commit()
            logger.warning(
                f"ALERT created for {endpoint.url}"
            )
    # Recovery Logging 
    if success:

        logger.info(
            f"Endpoint recovered: {endpoint.url}"
        )   
    return check
