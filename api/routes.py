from fastapi import APIRouter
from engine.decision_engine import top_convictions

router = APIRouter()

@router.get("/top")

def get_top():

    return top_convictions()
