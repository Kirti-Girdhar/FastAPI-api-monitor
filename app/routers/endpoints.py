from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.dependencies import get_current_user 
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.endpoint import EndpointCreate,EndpointResponse
from app.models.endpoint import Endpoint
from app.models.users import User
from app.services.monitoring_service import check_endpoint


router = APIRouter(
    prefix="/endpoints"
)

@router.get("/protected")
def protected(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.email}"}

@router.post("/",response_model=EndpointResponse)
def create_endpoint(endpoint:EndpointCreate,db:Session= Depends(get_db), user:User=Depends(get_current_user)):
    # new_endpoint=Endpoint(name=endpoint.name,url=endpoint.url,method=endpoint.method, check_interval=endpoint.check_interval,user_id=user.id)
    new_endpoint=Endpoint(**endpoint.dict(),user_id=user.id)
    db.add(new_endpoint)
    db.commit()
    db.refresh(new_endpoint)

    return new_endpoint

@router.get("/")
def get_endpoints(db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    points= db.query(Endpoint).filter(Endpoint.user_id==user.id).all()
    # points= db.query(Endpoint).all()

    return points

@router.delete("/{id}")
def delete_endpoint(id:int,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    endpoint=db.query(Endpoint).filter(Endpoint.id==id).first()
    if endpoint== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"endpoint with id: {id} does not exist")
    
    if endpoint.user_id!= user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not authorized to perform requested action")

    db.delete(endpoint)
    db.commit()

    return {"message":"Deleted"}


@router.post("/{id}/check")
async def run_check(id:int, db:Session= Depends(get_db),user= Depends(get_current_user)):
    endpoint=db.query(Endpoint).filter(Endpoint.id== id).first()

    if not endpoint:
        return {"error": "Endpoint not found"}
    result=await check_endpoint(endpoint,db)
    return {
        "status_code":result.status_code,
        "response_time":result.response_time,
        "success":result.success
            }