from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.CRUD_Visitante import VisitanteConnection
from schema.Visiatante_schema import Visitante

router = APIRouter(tags=["visitante"])
conn = VisitanteConnection()

@router.get("/listar", operation_id="listar_api_visitantes_get", status_code=HTTP_200_OK)
def listar_visitantes():
    items = []
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "nombre": data[1],
            "apellidos": data[2],
            "edad": data[3],
            "cedula": data[4],
            "relacion_paciente": data[5]
        }
        items.append(dictionary)
    return items

@router.get("/{id}", operation_id="get_one_api_visitantes_get", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Visitante no encontrado")
    dictionary = {
        "id": data[0],
        "nombre": data[1],
        "apellidos": data[2],
        "edad": data[3],
        "cedula": data[4],
        "relacion_paciente": data[5]
    }
    return dictionary

@router.post("/insert", operation_id="insert_api_visitantes_post", status_code=HTTP_201_CREATED)
def insert(visitante_data: Visitante):
    data = visitante_data.model_dump()
    data.pop("id", None)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{id}", operation_id="delete_api_visitantes_delete", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{id}", operation_id="update_api_visitantes_put", status_code=HTTP_204_NO_CONTENT)
def update(visitante_data: Visitante, id: int):
    data = visitante_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
