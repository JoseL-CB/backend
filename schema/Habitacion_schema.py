from pydantic import BaseModel
from typing import Optional

class Habitacion(BaseModel):
    id: Optional[int] = None
    num_habitacion: int
    tipo: str
    estado: str
    num_cama: int
