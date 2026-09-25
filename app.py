import flet as ft
from models import Produto
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONN = f"sqlite:///{os.path.join(BASE_DIR, 'Projeto.db')}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
Session = Session()
Base = declarative_base()



def main(page: ft.Page):

   lista_produtos = ft.ListView()
   
   def cadastrar(e):
      novo_produto = Produto(titulo=produto.value, preco=preco.value)
      Session.add(novo_produto)
      Session.commit()
      lista_produtos.controls.append(ft.Container(
                   ft.Text(p.titulo),
                   bgcolor=ft.Colors.BLACK_12,
                   padding=15,
                   alignment=ft.Alignment.CENTER,
                   margin=3,
                   border_radius=10
                   ) )

      
      page.update()
      print("produto salvo com sucesso.")

   page.title = "Cadastro"
   txt_titulo = ft.Text("Nome do produto")
   produto = ft.TextField(label= "Digite o nome do produto", text_align=ft.TextAlign.LEFT)
   txt_preco = ft.Text("Preço do Produto")
   preco = ft.TextField(value="0", label= "Digite o preço",text_align=ft.TextAlign.LEFT )
   btn_produto = ft.Button(content="Cadastrar", on_click=cadastrar)
               
    
   page.add(txt_titulo,
            produto,
            txt_preco,
            preco,
            btn_produto,
            
   )

   for p in Session.query(Produto).all():
      lista_produtos.controls.append(
         ft.Container(
             ft.Text(p.titulo),
             bgcolor=ft.Colors.BLACK_12,
             padding=15,
             alignment=ft.Alignment.CENTER,
             margin=3,
             border_radius=10
             ) 
         
         )

   page.add(

      lista_produtos,
   )

ft.run(main)