from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT,HTTP_401_UNAUTHORIZED
from models.CRUD_USUARIO import UserConnection
from schema.perfil_usuario_schema import perfilUsuario  # Corregir la importación
from schema.Login_schema import LoginSchema  # Importa el esquema de login

router = APIRouter(tags=["PerfilUsuario"])
conn = UserConnection()

@router.post("/login", status_code=HTTP_200_OK)
def login(credentials: LoginSchema):
    cedula = credentials.cedula
    password = credentials.password

    # Verificar las credenciales en la base de datos
    user = conn.verify_credentials(cedula, password)

    if user:
        return {"success": True, "role": user[8]}  # Asumiendo que 'roleid' es el noveno elemento en la tupla
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")

@router.get("/listar", status_code=HTTP_200_OK)
def root():
    items = []
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "nombres": data[1],
            "apellidos": data[2],
            "fecha_nacimiento": data[3],
            "cedula": data[4],
            "email": data[5],
            "password": data[6],
            "sexo": data[7],
            "roleid": data[8]
        }
        items.append(dictionary)
    return items

@router.get("/perfil_usuario/{id}", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="User not found")
    dictionary = {
        "id": data[0],
        "nombres": data[1],
        "apellidos": data[2],
        "fecha_nacimiento": data[3],
        "cedula": data[4],
        "email": data[5],
        "password": data[6],
        "sexo": data[7],
        "roleid": data[8]
    }
    return dictionary

@router.post("/insert", status_code=HTTP_201_CREATED)
def insert(user_data: perfilUsuario):  # Corregir el tipo de datos
    data = user_data.model_dump()
    data.pop("id", None)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{id}", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{id}", status_code=HTTP_204_NO_CONTENT)
def update(user_data: perfilUsuario, id: int):  # Corregir el tipo de datos
    data = user_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
