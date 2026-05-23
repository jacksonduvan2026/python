from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


lista_clientes = []


class Cliente(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None


@app.get("/clientes")
def listar_clientes():
    return lista_clientes


@app.post("/clientes")
def agregar_cliente(cliente: Cliente):

    lista_clientes.append(cliente)

    return {
        "mensaje": "Cliente agregado correctamente"
    }


@app.put("/clientes/{id}")
def actualizar_cliente(id: int, cliente_actualizado: Cliente):

    for i, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            lista_clientes[i] = cliente_actualizado

            return {
                "mensaje": "Cliente actualizado"
            }

    return {
        "error": "Cliente no encontrado"
    }


@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for i, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            lista_clientes.pop(i)

            return {
                "mensaje": "Cliente eliminado"
            }

    return {
        "error": "Cliente no encontrado"
    }
    