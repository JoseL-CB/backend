from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.CRUD_Paciente import PacienteConnection
from schema.Paciente_schema import Paciente

router = APIRouter(tags=["Pacientes"])
conn = PacienteConnection()

@router.get("/listar", operation_id="listar_api_paciente_get", status_code=HTTP_200_OK)
def listar_pacientes():
    items = []
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "estado": data[1],
            "nombres": data[2],
            "apellidos": data[3],
            "cedula": data[4],
            "fecha_nacimiento": data[5]
        }
        items.append(dictionary)
    return items

@router.get("/{id}", operation_id="get_one_api_paciente_get", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    dictionary = {
        "id": data[0],
        "estado": data[1],
        "nombres": data[2],
        "apellidos": data[3],
        "cedula": data[4],
        "fecha_nacimiento": data[5]
    }
    return dictionary

@router.post("/insert", operation_id="insert_api_paciente_post", status_code=HTTP_201_CREATED)
def insert(paciente_data: Paciente):
    data = paciente_data.model_dump()
    data.pop("id", None)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{id}", operation_id="delete_api_paciente_delete", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{id}", operation_id="update_api_paciente_put", status_code=HTTP_204_NO_CONTENT)
def update(paciente_data: Paciente, id: int):
    data = paciente_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
