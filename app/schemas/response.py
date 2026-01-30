from pydantic import BaseModel


class ChurnResponse(BaseModel):

    churn_probability: float
    risk_level: str
    recommended_action: str
