from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class RegistroVisitas(BaseModel):
    id: Optional[int] = None
    fecha_entrada: date
    hora_entrada: time
    idvisitante: int
    idpaciente: int
    fecha_salida: Optional[date] = None
    hora_salida: Optional[time] = None
