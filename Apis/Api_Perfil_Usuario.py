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

    print(f"Recibido cedula: {cedula}, password: {password}")  # Añadir log

    # Verificar las credenciales en la base de datos
    user = conn.verify_credentials(cedula, password)

    if user:
        print("Usuario encontrado:", user)
        # Asumiendo que user[8] es el roleid y se puede mapear a un nombre de rol
        role_mapping = {1: "Admin", 2: "Recepcionista", 3: "Guarda"}
        role_name = role_mapping.get(user[8], "Unknown")
        return {"success": True, "role": user[8], "role_name": role_name, "nombre": user[1]}
    else:
        print("Credenciales incorrectas")
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")

    
# Ruta para cerrar sesión
@router.post("/logout", status_code=HTTP_204_NO_CONTENT)
def logout():
    # No se necesita ningún parámetro, simplemente eliminamos la información de usuario del almacenamiento
    # Puedes agregar cualquier otra lógica de limpieza aquí si es necesario
    return Response(status_code=HTTP_204_NO_CONTENT)

# Define el mapeo de roles
ROLES_MAPPING = {
    1: "Admin",
    2: "Recepcionista",
    3: "Guarda"
}

@router.get("/listar", status_code=HTTP_200_OK)
def root():
    items = []
    for data in conn.read_all():
        user_dict = {
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
        # Reemplaza roleid con el nombre del rol correspondiente
        user_dict["rol"] = ROLES_MAPPING.get(user_dict["roleid"], "Desconocido")
        del user_dict["roleid"]  # Elimina el campo roleid
        items.append(user_dict)
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
