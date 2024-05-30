from pydantic import BaseModel
from typing import Optional
from datetime import date

class Paciente(BaseModel):
    id: Optional[int] = None
    estado: str
    nombres: str
    apellidos: str
    cedula: int
    fecha_nacimiento: date
