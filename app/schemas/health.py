from pydantic import BaseModel
from typing import Literal

class HealthResponse(BaseModel):
    status: Literal["ok"]