from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.CRUD_EstadoPaciente import EstadoPacienteConnection
from schema.EstadoPaciente_schema import EstadoPaciente

router = APIRouter(tags=["EstadoPaciente"])
conn = EstadoPacienteConnection()

@router.get("/listar", operation_id="listar_api_estado_paciente_get", status_code=HTTP_200_OK)
def listar_estados():
    items = []
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "nombre": data[1]
        }
        items.append(dictionary)
    return items

@router.get("/{id}", operation_id="get_one_api_estado_paciente_get", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    dictionary = {
        "id": data[0],
        "nombre": data[1]
    }
    return dictionary

@router.post("/insert", operation_id="insert_api_estado_paciente_post", status_code=HTTP_201_CREATED)
def insert(estado_data: EstadoPaciente):
    data = estado_data.model_dump()
    data.pop("id", None)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{id}", operation_id="delete_api_estado_paciente_delete", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{id}", operation_id="update_api_estado_paciente_put", status_code=HTTP_204_NO_CONTENT)
def update(estado_data: EstadoPaciente, id: int):
    data = estado_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
