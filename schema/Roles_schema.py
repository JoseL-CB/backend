from pydantic import BaseModel
from typing import Optional

class Roles(BaseModel):
    id: Optional[int] = None
    namerol: str