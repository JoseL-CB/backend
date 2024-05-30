from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class Hospitalizacion(BaseModel):
    id: Optional[int] = None
    fecha_hospitalizacion: date
    hora_hospitalizacion: time
    idpaciente: int
    idhabitacion: int
    fecha_alta: Optional[date] = None
    hora_alta: Optional[time] = None
