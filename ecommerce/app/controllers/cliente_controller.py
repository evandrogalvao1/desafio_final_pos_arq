from flask import jsonify, request
from ..services.cliente_service import ClienteService

def count_clientes():
    total = ClienteService.count_clientes()
    return jsonify({"total_clientes": total})

def find_all_clientes():
    clientes = ClienteService.find_all_clientes()
    return jsonify(clientes)

def find_cliente_by_id(id):
    cliente = ClienteService.find_cliente_by_id(id)
    return jsonify(cliente)

def find_clientes_by_name(nome):
    clientes = ClienteService.find_clientes_by_name(nome)
    return jsonify(clientes)

def create_cliente():
    data = request.get_json()
    cliente = ClienteService.create_cliente(data)
    return jsonify(cliente), 201

def update_cliente(id):
    data = request.get_json()
    cliente = ClienteService.update_cliente(id, data)
    return jsonify(cliente)

def delete_cliente(id):
    ClienteService.delete_cliente(id)
    return '', 204