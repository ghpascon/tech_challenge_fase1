from typing import Optional
from pydantic import BaseModel, field_validator

class EmbrapaRequestAno(BaseModel):
    ano: Optional[int] = None

    @field_validator('ano')
    def validar_ano(cls, v):
        if v is None:
            return 2023
        if v < 1970 or v > 2023:
            return 2023
        return v
