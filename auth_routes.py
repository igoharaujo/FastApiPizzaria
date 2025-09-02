from fastapi import APIRouter, Depends, HTTPException
from main import bcrypt_context
from models import  Usuario
from dependencies import pegar_sessao
from schema import  UsuarioSchema
from sqlalchemy.orm import Session
auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotas dos pedidos precisam de atutenticação.
    :return:
    """
    return {"mensagem": "Vc acessou a area"}



@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return  {"mensagem": f"Conta criada com sucesso - {usuario_schema.email}"}