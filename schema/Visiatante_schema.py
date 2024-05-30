from pydantic import BaseModel
from typing import Optional

class Visitante(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellidos: str
    edad: int
    cedula: int
    relacion_paciente: str
