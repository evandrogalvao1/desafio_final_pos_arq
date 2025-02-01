from flask import Blueprint
from .controllers.cliente_controller import (
    count_clientes, find_all_clientes, find_cliente_by_id, find_clientes_by_name,
    create_cliente, update_cliente, delete_cliente
)

cliente_bp = Blueprint('cliente', __name__)

# Novos endpoints
@cliente_bp.route('/clientes/count', methods=['GET'])
def count_clientes_route():
    return count_clientes()

@cliente_bp.route('/clientes/findAll', methods=['GET'])
def find_all_clientes_route():
    return find_all_clientes()

@cliente_bp.route('/clientes/findById/<int:id>', methods=['GET'])
def find_cliente_by_id_route(id):
    return find_cliente_by_id(id)

@cliente_bp.route('/clientes/findByName/<string:nome>', methods=['GET'])
def find_clientes_by_name_route(nome):
    return find_clientes_by_name(nome)

# Endpoints existentes
@cliente_bp.route('/clientes', methods=['POST'])
def add_cliente():
    return create_cliente()

@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def modify_cliente(id):
    return update_cliente(id)

@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def remove_cliente(id):
    return delete_cliente(id)

def init_routes(app):
    app.register_blueprint(cliente_bp, url_prefix='/api')