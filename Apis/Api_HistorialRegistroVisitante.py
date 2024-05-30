from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.CRUD_HistorialRegistroVisitante import HistorialRegistroVisitanteConnection
from schema.HistorialResgistroVisitante_schema import HistorialRegistroVisitante

router = APIRouter(tags=["HistorialRegistroVisitante"])
conn = HistorialRegistroVisitanteConnection()

@router.get("/listar", operation_id="listar_api_historial_get", status_code=HTTP_200_OK)
def listar_historial():
    items = []
    for data in conn.read_all():
        dictionary = {
            "idperfilusuario": data[0],
            "idregistrovisita": data[1]
        }
        items.append(dictionary)
    return items

@router.get("/{id}", operation_id="get_one_api_historial_get", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    dictionary = {
        "idperfilusuario": data[0],
        "idregistrovisita": data[1]
    }
    return dictionary

@router.post("/insert", operation_id="insert_api_historial_post", status_code=HTTP_201_CREATED)
def insert(historial_data: HistorialRegistroVisitante):
    data = historial_data.model_dump()
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{idperfilusuario}/{idregistrovisita}", operation_id="delete_api_historial_delete", status_code=HTTP_204_NO_CONTENT)
def delete(idperfilusuario: int, idregistrovisita: int):
    conn.delete(idperfilusuario, idregistrovisita)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{idperfilusuario}", operation_id="update_api_historial_put", status_code=HTTP_204_NO_CONTENT)
def update(historial_data: HistorialRegistroVisitante, idperfilusuario: int):
    data = historial_data.model_dump()
    data["idperfilusuario"] = idperfilusuario
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
