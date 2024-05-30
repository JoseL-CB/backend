from pydantic import BaseModel
from typing import Optional
from datetime import date

class perfilUsuario(BaseModel):
    id: Optional[int]=None
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    cedula: int
    email: str
    password: str
    sexo: str
    roleid:Optional[int]
