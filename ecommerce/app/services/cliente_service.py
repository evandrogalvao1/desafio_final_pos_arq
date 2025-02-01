from ..models.cliente import Cliente
from .. import db

class ClienteService:
    @staticmethod
    def count_clientes():
        return Cliente.query.count()

    @staticmethod
    def find_all_clientes():
        clientes = Cliente.query.all()
        return [cliente.to_dict() for cliente in clientes]

    @staticmethod
    def find_cliente_by_id(id):
        cliente = Cliente.query.get_or_404(id)
        return cliente.to_dict()

    @staticmethod
    def find_clientes_by_name(nome):
        clientes = Cliente.query.filter(Cliente.nome.ilike(f'%{nome}%')).all()
        return [cliente.to_dict() for cliente in clientes]

    @staticmethod
    def create_cliente(data):
        cliente = Cliente(
            nome=data['nome'],
            email=data['email'],
            telefone=data.get('telefone')
        )
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_dict()

    @staticmethod
    def update_cliente(id, data):
        cliente = Cliente.query.get_or_404(id)
        cliente.nome = data.get('nome', cliente.nome)
        cliente.email = data.get('email', cliente.email)
        cliente.telefone = data.get('telefone', cliente.telefone)
        db.session.commit()
        return cliente.to_dict()

    @staticmethod
    def delete_cliente(id):
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return None