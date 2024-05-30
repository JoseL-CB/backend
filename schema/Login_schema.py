# schema/login_schema.py
from pydantic import BaseModel

class LoginSchema(BaseModel):
    cedula: str
    password: str
