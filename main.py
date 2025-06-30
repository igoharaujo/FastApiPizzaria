from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

"""
Endpoint: É uma rota (Endereço) que um sistema oferece para que outro sistema,
possa interagir com ele.
- Se associa a um método, GET, POST, PATCH ou DELETE
- Cada endpoint realiza uma ação espeficica como enviar, pegar, atualizar ou deleter
informações.

--------------
Criação das rotas:
- auth
- Orders

"""


app.include_router(auth_router)
app.include_router(order_router)