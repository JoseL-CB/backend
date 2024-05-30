from pydantic import BaseModel
from typing import Optional

class EstadoPaciente(BaseModel):
    id: Optional[int] = None
    nombre: str
