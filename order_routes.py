from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from models import Pedido
from schema import  PedidoSchema
from models import Pedido
order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])


@order_router.get("/")
async def pedidos():
    return {"mensagem": "Vc acessou a area de pedidos!"}

@order_router.get("/teste")
async def teste():
    return {"mensagem": "Vc acessou a area de teste!"}

@order_router.post("/pedido")
async def pedido(Pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=Pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"pediodo criado com sucesso!"}