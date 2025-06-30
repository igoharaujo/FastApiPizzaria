from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import declarative_base
#from alembic import 

db = create_engine("sqlite:///banco.db")

Base = declarative_base()


# Clesses/Tabelas do banco

class Usuario(Base):
    __tablename__ = "usuarios"

    id     = Column("id", Integer, primary_key=True, autoincrement=True)
    nome   = Column("nome", String)
    email  = Column("email", String)
    senha  = Column("senha", String)
    ativo  = Column("ativo", Boolean)
    admin  = Column("admin", Boolean, default=False)


    def __init__(self, nome, email, senha, ativo, admin=False):
        self.nome   = nome
        self.email  = email
        self.senha  = senha
        self.ativo  = ativo
        self.admin  = admin


class Pedido(Base):
    __tablename__ = "pedidos"

    #STATUS_PEDIDOS = (("PENDENTE", "PENDENTES"), ("CANCELADOS", "CANCELADOS"), ("FINALIZADO", "FINALIZADO"))

    id      = Column("id", Integer, primary_key=True, autoincrement=True)
    status  = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco   = Column("preco", Float)

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status  = status
        self.preco   = preco


class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id              = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade      = Column("quantidade", Integer)
    sabor           = Column("sabor", String)
    tamanho         = Column("tamanho", String)
    preco_unitario  = Column("preco_unitario", Float)
    Pedido          = Column("pedido", ForeignKey("pedidos.id"))


    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade     = quantidade
        self.sabor          = sabor
        self.tamanho        = tamanho
        self.preco_unitario = preco_unitario
        self.Pedido         = pedido