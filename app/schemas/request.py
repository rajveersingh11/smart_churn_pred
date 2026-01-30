from pydantic import BaseModel
from typing import List


class ChurnRequest(BaseModel):

    features: List[float]
