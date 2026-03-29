import httpx
import time

from sqlalchemy.orm import Session

from app.models.check import Check
from app.models.alert import Alert


async def check_endpoint(endpoint, db: Session):

    start_time = time.time()

    success = False
    status_code = None

    try:
        async with httpx.AsyncClient() as client:

            response = await client.request(
                method=endpoint.method,
                url=endpoint.url,
                timeout=5
            )

        status_code = response.status_code

        if status_code < 400:
            success = True

    except Exception:
        success = False

    response_time = time.time() - start_time

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

    if len(last_checks) == 3 and all(not c.success for c in last_checks):
        # print("ALERT: Endpoint failed 3 times")
        alert=Alert(endpoint_id=endpoint.id,
                    message="Endpoint failed 3 consecutive times")

        db.add(alert)
        db.commit()
    return check
