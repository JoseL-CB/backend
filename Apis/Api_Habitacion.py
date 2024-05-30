from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.CRUD_Habitacion import HabitacionConnection
from schema.Habitacion_schema import Habitacion

router = APIRouter(tags=["Habitacion"])
conn = HabitacionConnection()

@router.get("/listar", operation_id="listar_api_habitacion_get", status_code=HTTP_200_OK)
def listar_habitaciones():
    items = []
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "num_habitacion": data[1],
            "tipo": data[2],
            "estado": data[3],
            "num_cama": data[4]
        }
        items.append(dictionary)
    return items

@router.get("/{id}", operation_id="get_one_api_habitacion_get", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    dictionary = {
        "id": data[0],
        "num_habitacion": data[1],
        "tipo": data[2],
        "estado": data[3],
        "num_cama": data[4]
    }
    return dictionary

@router.post("/insert", operation_id="insert_api_habitacion_post", status_code=HTTP_201_CREATED)
def insert(habitacion_data: Habitacion):
    data = habitacion_data.model_dump()
    data.pop("id", None)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{id}", operation_id="delete_api_habitacion_delete", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{id}", operation_id="update_api_habitacion_put", status_code=HTTP_204_NO_CONTENT)
def update(habitacion_data: Habitacion, id: int):
    data = habitacion_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
