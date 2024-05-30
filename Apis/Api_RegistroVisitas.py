from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.CRUD_RegistroVisitas import RegistroVisitasConnection
from schema.RegistroVisitas_schema import RegistroVisitas


router = APIRouter(tags=["RegistroVisitas"])
conn = RegistroVisitasConnection()

@router.get("/listar", operation_id="listar_api_registrovisitas_get", status_code=HTTP_200_OK)
def listar_registrovisitas():
    items = []
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "fecha_entrada": data[1],
            "hora_entrada": data[2],
            "idvisitante": data[3],
            "idpaciente": data[4],
            "fecha_salida": data[5],
            "hora_salida": data[6]
        }
        items.append(dictionary)
    return items

@router.get("/{id}", operation_id="get_one_api_registrovisitas_get", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Registro de visita no encontrado")
    dictionary = {
        "id": data[0],
        "fecha_entrada": data[1],
        "hora_entrada": data[2],
        "idvisitante": data[3],
        "idpaciente": data[4],
        "fecha_salida": data[5],
        "hora_salida": data[6]
    }
    return dictionary

@router.post("/insert", operation_id="insert_api_registrovisitas_post", status_code=HTTP_201_CREATED)
def insert(registrovisitas_data: RegistroVisitas):
    data = registrovisitas_data.model_dump()
    data.pop("id", None)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{id}", operation_id="delete_api_registrovisitas_delete", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{id}", operation_id="update_api_registrovisitas_put", status_code=HTTP_204_NO_CONTENT)
def update(registrovisitas_data: RegistroVisitas, id: int):
    data = registrovisitas_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
