from pydantic import BaseModel
class Mensagem(BaseModel):
    titulo: str
    conteudo: str
    publicada: bool = True

class Menu_msg(BaseModel):
    menuNav: str  # Título do item no menu
    link: str = None  # Link opcional
