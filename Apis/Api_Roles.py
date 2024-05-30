from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from models.CRUD_Roles import RolesConnection
from schema.Roles_schema import Roles

router = APIRouter(tags=["Roles"])
conn = RolesConnection()

@router.get("/listar", operation_id="listar_api_roles_get", status_code=HTTP_200_OK)
def listar_roles():
    items = []
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "namerol": data[1]
        }
        items.append(dictionary)
    return items

@router.get("/{id}", operation_id="get_one_api_roles_get", status_code=HTTP_200_OK)
def get_one(id: int):
    data = conn.read_one(id)
    if data is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    dictionary = {
        "id": data[0],
        "namerol": data[1]
    }
    return dictionary

@router.post("/insert", operation_id="insert_api_roles_post", status_code=HTTP_201_CREATED)
def insert(roles_data: Roles):
    data = roles_data.model_dump()
    data.pop("id", None)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@router.delete("/delete/{id}", operation_id="delete_api_roles_delete", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put("/update/{id}", operation_id="update_api_roles_put", status_code=HTTP_204_NO_CONTENT)
def update(roles_data: Roles, id: int):
    data = roles_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)
