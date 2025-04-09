import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")

# Janela principal
root = ctk.CTk()  # Cria a janela principal com CustomTkinter
root.geometry("375x667")  # Define o tamanho da janela
root.title("Login")  # Define o título da janela
root.resizable(False, False)  # Impede que o usuário redimensione a janela

# Imagem de fundo
bg_image = Image.open("images/login.png")  # Abre a imagem do fundo
bg_image = ImageTk.PhotoImage(bg_image)  # Converte a imagem para uso no Tkinter

bg_label = ctk.CTkLabel(master=root,
                        image=bg_image,
                        text=""  # Remove qualquer texto sobre a imagem
                        )
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Preenche toda a janela com a imagem

# Campo de entrada para o nome de usuário
usuario_entrada = ctk.CTkEntry(
    master=root,
    placeholder_text='Usuário',  # Texto exibido como dica
    placeholder_text_color='black',  # Cor da dica
    fg_color='#BBBBBB',  # Cor de fundo do campo
    text_color='black',  # Cor do texto digitado
    width=208,
    height=33
)
usuario_entrada.place(relx=0.5, rely=0.48, anchor="center")  # Centraliza na vertical em 48%

# Campo de entrada para a senha
senha_entrada = ctk.CTkEntry(
    master=root,
    placeholder_text='Senha',
    placeholder_text_color='black',
    fg_color='#BBBBBB',
    text_color='black',
    show="*",  # Oculta o texto digitado (como senha)
    width=208,
    height=33
)
senha_entrada.place(relx=0.5, rely=0.56, anchor="center")  # Centraliza na vertical em 56%

# Caixa de seleção "Lembrar senha"
lembrar_senha = ctk.CTkCheckBox(
    master=root,
    fg_color='#BBBBBB',        # Cor do quadrado de seleção
    hover_color='#BBBBBB',     # Cor ao passar o mouse
    text='Lembrar senha',
    text_color='black',
    checkbox_height=20,        # Altura da caixa
    checkbox_width=20,         # Largura da caixa
    checkmark_color='black',   # Cor da marca de seleção
    bg_color='#F3F3F3'         # Cor de fundo por trás da caixa
)
lembrar_senha.place(relx=0.4, rely=0.62, anchor="center")  # Posiciona a caixa

# Adicionando a imagem de "olho"
eye_open_img = ctk.CTkImage(Image.open("images/eye_open.png").resize((20, 20)))
eye_closed_img = ctk.CTkImage(Image.open("images/eye_closed.png").resize((20, 20)))

# Função para alterar entre mostrar e esconder
show_password = [False]  # uso uma lista para alterar dentro da função

def toggle_password():
    if show_password[0]:
        senha_entrada.configure(show="*")
        eye_button.configure(image=eye_closed_img)
    else:
        senha_entrada.configure(show="")
        eye_button.configure(image=eye_open_img)
    show_password[0] = not show_password[0]

# Botão com imagem do olho
eye_button = ctk.CTkButton(
    master=root,            # qual tela que o botão vai ser adicionado
    width=20,               # largura
    height=20,              # altura
    image=eye_closed_img,   # imagem que ele vai começar mostrando
    text="",                # Texto, no caso, nenhum
    fg_color="#BBBBBB",     # Fundo "invisível" usando a mesma cor da entrada
    hover_color="grey",     # Sem cor ao passar o mouse
    border_width=0,         # Sem borda
    corner_radius=0,        # Sem canto arredondado
    command=toggle_password # Aqui ele "puxa" a função de alternar a senha
)

eye_button.place(x=262, y=360)  # Ajuste manual da posição, colocando ele dentro da entrada "senha no canto"

# Botão de entrada (login)
entrar_button = ctk.CTkButton(
    master=root,
    width=164,
    height=41,
    text='Entrar',
    text_color='Black',
    fg_color='#BBBBBB',  # Cor de fundo do botão
    border_width=1,      # Largura da borda do botão
    border_color='black', # Cor da borda do botão
    hover_color='grey',  # Cor ao passar o mouse
    cursor='hand2' # Muda o cursor para uma mãozinha ao passar o mouse
)
entrar_button.place(relx=0.5,
                    rely=0.68,
                    anchor="center"  # Centraliza o botão na posição
                    )

# Frame para agrupar o texto "Não tem uma conta?" e o link "Crie aqui."
frame = ctk.CTkFrame(
    master=root,
    fg_color='#F3F3F3'  # Cor de fundo do frame
)
frame.place(relx=0.5, rely=0.74, anchor="center")  # Posiciona o frame centralizado

# Label informativo (parte estática)
label1 = ctk.CTkLabel(master=frame,
                      text='Não tem uma conta?',
                      text_color='black'  # Cor do texto
                      )
label1.pack(side="left")  # Posiciona à esquerda dentro do frame

# Função que será chamada ao clicar no texto "Crie aqui."
def abrir_cadastro():  # TESTE TESTE TESTE
    print('Abrindo cadastro')  # Apenas um print por enquanto

# Label clicável (simula um link)
label2 = ctk.CTkLabel(master=frame,
                      text=' Crie aqui.',
                      text_color='blue',  # Cor azul para parecer um link
                      cursor="hand2",     # Muda o cursor para uma mãozinha ao passar o mouse
                      font=ctk.CTkFont(family="Arial", size=12, underline=True)  # Texto sublinhado
                      )
label2.pack(side="left")  # Posiciona à esquerda, ao lado do label1

# Associa o clique do mouse (botão 1) à função abrir_cadastro
label2.bind("<Button-1>", lambda e: abrir_cadastro())




root.mainloop()
