from fastapi import APIRouter

router = APIRouter()

# Example route
@router.get("/")
def read_payments():
    return {"message": "Payments route working"}
