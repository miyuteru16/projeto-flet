import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONN = f"sqlite:///{os.path.join(BASE_DIR, 'Projeto.db')}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
Session = Session()
Base = declarative_base()

class Produto(Base):
    __tablename__ = "Produto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    preco = Column(Float())

Base.metadata.create_all(engine)