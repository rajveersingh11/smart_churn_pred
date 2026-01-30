from fastapi import APIRouter, Depends, HTTPException

from app.schemas.request import ChurnRequest
from app.schemas.response import ChurnResponse
from app.services.decision_engine import DecisionEngine
from app.core.security import verify_token


router = APIRouter()

engine = DecisionEngine()


@router.post("/predict", response_model=ChurnResponse)
def predict(
    req: ChurnRequest,
    token: str = Depends(verify_token)
):

    try:

        result = engine.make_decision(req.features)

        return ChurnResponse(**result)

    except Exception:

        raise HTTPException(500, "Prediction failed")
