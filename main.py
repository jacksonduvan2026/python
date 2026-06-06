from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


lista_clientes = []
lista_facturas = []
lista_transacciones = []





class Cliente(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None


class Factura(BaseModel):
    id: int
    fecha: str
    valor_total: float
    cliente: str


class Transaccion(BaseModel):
    id: int
    vr_unitario: float
    cantidad: int
    factura_id: int



# CRUD CLIENTES


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



# CRUD FACTURAS


@app.get("/facturas")
def listar_facturas():
    return lista_facturas


@app.post("/facturas")
def agregar_factura(factura: Factura):

    lista_facturas.append(factura)

    return {
        "mensaje": "Factura agregada correctamente"
    }


@app.put("/facturas/{id}")
def actualizar_factura(id: int, factura_actualizada: Factura):

    for i, factura in enumerate(lista_facturas):

        if factura.id == id:

            lista_facturas[i] = factura_actualizada

            return {
                "mensaje": "Factura actualizada"
            }

    return {
        "error": "Factura no encontrada"
    }


@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for i, factura in enumerate(lista_facturas):

        if factura.id == id:

            lista_facturas.pop(i)

            return {
                "mensaje": "Factura eliminada"
            }

    return {
        "error": "Factura no encontrada"
    }



# CRUD TRANSACCIONES

ñ
@app.get("/transacciones")
def listar_transacciones():
    return lista_transacciones


@app.post("/transacciones")
def agregar_transaccion(transaccion: Transaccion):

    lista_transacciones.append(transaccion)

    return {
        "mensaje": "Transacción agregada correctamente"
    }


@app.put("/transacciones/{id}")
def actualizar_transaccion(id: int, transaccion_actualizada: Transaccion):

    for i, transaccion in enumerate(lista_transacciones):

        if transaccion.id == id:

            lista_transacciones[i] = transaccion_actualizada

            return {
                "mensaje": "Transacción actualizada"
            }

    return {
        "error": "Transacción no encontrada"
    }


@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    for i, transaccion in enumerate(lista_transacciones):

        if transaccion.id == id:

            lista_transacciones.pop(i)

            return {
                "mensaje": "Transacción eliminada"
            }

    return {
        "error": "Transacción no encontrada"
    }