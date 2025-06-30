from fastapi import APIRouter


#Roteador
order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

#Rotas:
@order_router.get("/")
async def pedidos():
    return {"mensagem": "Hello Word"}
