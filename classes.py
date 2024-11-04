from pydantic import BaseModel
class Mensagem(BaseModel):
    titulo: str
    conteudo: str
    publicada: bool = True

class Menu_msg(BaseModel):
    menuNav: str  # Título do item no menu
    link: str = None  # Link opcional

class VendaBase(BaseModel):
    nome_cliente: str
    cpf: str
    produtos: str

class VendaCreate(VendaBase):
    pass

class VendaUpdate(VendaBase):
    pass

class VendaOut(VendaBase):
    id: int

    class Config:
        orm_mode = True
