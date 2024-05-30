from pydantic import BaseModel

class HistorialRegistroVisitante(BaseModel):
    idperfilusuario: int
    idregistrovisita: int
