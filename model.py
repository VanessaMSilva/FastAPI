from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from database import Base
from datetime import datetime

class Model_Mensagem(Base):
    __tablename__ = 'teste'
    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    publicada = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class Model_Menu(Base):
    __tablename__ = 'menu'
    
    id = Column(Integer, primary_key=True, nullable=False)
    menuNav = Column(String, nullable=False)
    link = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    
class Model_Venda(Base):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, index=True)
    nome_cliente = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    produtos = Column(String)