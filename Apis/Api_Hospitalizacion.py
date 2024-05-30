from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.CRUD_Hospitalizacion import HospitalizacionConnection
from schema.Hospitalizacion_schema import Hospitalizacion

router = APIRouter(tags=["Hozpitaizacion"])
conn = HospitalizacionConnection()

@router.get("/listar", operation_id="listar_api_hospitalizacion_get", status_code=HTTP_200_OK)
def listar_hospitalizaciones():
    items = []
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "fecha_hospitalizacion": data[1],
            "hora_hospitalizacion": data[2],
            "idpaciente": data[3],
            "idhabitacion": data[4],
            "fecha_alta": data[5],
            "hora_alta": data[6]
        }
        items.append(dictionary)
    return items

@router.get("/{id}", operation_id="get_one_api_hospitalizacion_get", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Hospitalización no encontrada")
    dictionary = {
        "id": data[0],
        "fecha_hospitalizacion": data[1],
        "hora_hospitalizacion": data[2],
        "idpaciente": data[3],
        "idhabitacion": data[4],
        "fecha_alta": data[5],
        "hora_alta": data[6]
    }
    return dictionary

@router.post("/insert", operation_id="insert_api_hospitalizacion_post", status_code=HTTP_201_CREATED)
def insert(hospitalizacion_data: Hospitalizacion):
    data = hospitalizacion_data.model_dump()
    data.pop("id", None)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{id}", operation_id="delete_api_hospitalizacion_delete", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{id}", operation_id="update_api_hospitalizacion_put", status_code=HTTP_204_NO_CONTENT)
def update(hospitalizacion_data: Hospitalizacion, id: int):
    data = hospitalizacion_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
