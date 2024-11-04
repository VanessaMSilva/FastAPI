from fastapi import FastAPI, Depends, status, HTTPException
import model
import webScraping
import bus050
import intercampi 
from database import engine, get_db
from sqlalchemy.orm import Session
import classes
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "lala"}

@app.get("/menu/", status_code=status.HTTP_201_CREATED)
def criar_valores(db: Session = Depends(get_db)):
    # Chama a função de scraping para obter os dados
    dados = webScraping.return_dado()
    if not dados:
        raise HTTPException(status_code=400, detail="Erro ao coletar dados do menu")
    # Itera sobre os dados retornados pelo web scraping e insere no banco
    mensagens_criadas = []
    
    print(f'{dados["menuNav"]}: {dados["link"]}')
    for i in range(len(dados["link"])):
        print(f'{dados["link"][i]}: {dados["menuNav"][i]}\n')
        nova_mensagem = model.Model_Menu(
            menuNav = dados["menuNav"][i],
            link = dados["link"][i],
        )
        db.add(nova_mensagem)
        db.commit()
        db.refresh(nova_mensagem)
        mensagens_criadas.append(nova_mensagem)
    return {"Mensagens": mensagens_criadas}
origins = [
 'http://localhost:5173'
]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=['*'],
 allow_headers=['*']
)

@app.get("/Horario/")
async def get_horarios() -> Dict[str, List[str]]:
    return {
        "horariosChegada050": bus050.get_horario_050(),
        "horariosSaidaIntercampi": intercampi.get_horario_intercampi()
    }

@app.get("/mensagens", response_model=List[classes.Menu_msg], status_code=status.HTTP_200_OK)
async def buscar_valores(db: Session = Depends(get_db), skip: int = 0, limit: int=100):
    mensagens = db.query(model.Model_Menu).offset(skip).limit(limit).all()
    return mensagens

@app.post("/vendas/", response_model=classes.VendaOut)
def cadastrar_venda(venda: classes.VendaCreate, db: Session = Depends(get_db)):
    db_venda = model.Model_Venda(nome_cliente=venda.nome_cliente, cpf=venda.cpf, produtos=venda.produtos)
    db.add(db_venda)
    db.commit()
    db.refresh(db_venda)
    return db_venda

# Rota para buscar uma venda pelo CPF
@app.get("/vendas/{cpf}", response_model=classes.VendaOut)
def buscar_venda(cpf: str, db: Session = Depends(get_db)):
    db_venda = db.query(model.Model_Venda).filter(model.Model_Venda.cpf == cpf).first()
    if not db_venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada.")
    return db_venda

# Rota para atualizar uma venda pelo CPF
@app.put("/vendas/{cpf}", response_model=classes.VendaOut)
def alterar_venda(cpf: str, venda: classes.VendaUpdate, db: Session = Depends(get_db)):
    db_venda = db.query(model.Model_Venda).filter(model.Model_Venda.cpf == cpf).first()
    if not db_venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada.")
    db_venda.nome_cliente = venda.nome_cliente
    db_venda.produtos = venda.produtos
    db.commit()
    db.refresh(db_venda)
    return db_venda

# Rota para excluir uma venda pelo CPF
@app.delete("/vendas/{cpf}", response_model=dict)
def excluir_venda(cpf: str, db: Session = Depends(get_db)):
    db_venda = db.query(model.Model_Venda).filter(model.Model_Venda.cpf == cpf).first()
    if not db_venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada.")
    db.delete(db_venda)
    db.commit()
    return {"message": "Venda excluída com sucesso."}
