from pydantic import BaseModel
from typing import Optional

class Visitante(BaseModel):
    id: Optional[int] = None
    nombres: str
    apellidos: str
    edad: int
    cedula: int
    relacion_paciente: str
