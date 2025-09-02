from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
#from sqlalchemy_utils import ChoiceType

# Criar a conexão com o banco
db = create_engine("sqlite:///banco.db")

# Criar a base do banco
Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(Base):
    __tablename__ = "pedidos"


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    #usuario_id = Column("usuario_id", Integer, ForeignKey("usuarios.id"))
    usuario = Column("usuario_id", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __init__(self, status="PENDENTE", usuario=None, preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco


class ItemPedido(Base):
    __tablename__ = "item_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido_id = Column("pedido_id", Integer, ForeignKey("pedidos.id"))
    pedido = relationship("Pedido")

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido


# Criar as tabelas no banco (caso não use Alembic)
# Base.metadata.create_all(db)
