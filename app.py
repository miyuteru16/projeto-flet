import flet as ft

def main(page: ft.Page):
   
   def cadastrar(e):
      print(produto.value)
      print(preco.value)

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
            btn_produto
            )

ft.run(main)