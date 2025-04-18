import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")

def tela_login():
    """
    Cria e exibe a interface gráfica da tela de login.

    A tela inclui:
    - Entrada de usuário e senha.
    - Opção de lembrar senha.
    - Botão de mostrar/ocultar senha.
    - Botão de login (ainda sem funcionalidade).
    - Link para a tela de cadastro.

    Returns:
        None
    """
    pagina_lg = ctk.CTk()
    pagina_lg.geometry("375x667")
    pagina_lg.title("Login")
    pagina_lg.resizable(False, False)
    pagina_lg.iconbitmap("images/icon.ico")

    fundo_imagem = Image.open("images/login.png")
    fundo_imagem = ctk.CTkImage(light_image=fundo_imagem, size=(375, 667))

    fundo_label = ctk.CTkLabel(master=pagina_lg, image=fundo_imagem)
    fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

    usuario_entrada = ctk.CTkEntry(
        master=pagina_lg,
        placeholder_text='Usuário',
        placeholder_text_color='black',
        fg_color='#BBBBBB',
        text_color='black',
        width=208,
        height=33
    )
    usuario_entrada.place(relx=0.5, rely=0.48, anchor="center")

    senha_entrada = ctk.CTkEntry(
        master=pagina_lg,
        placeholder_text='Senha',
        placeholder_text_color='black',
        fg_color='#BBBBBB',
        text_color='black',
        show="*",
        width=208,
        height=33
    )
    senha_entrada.place(relx=0.5, rely=0.56, anchor="center")

    lembrar_senha = ctk.CTkCheckBox(
        master=pagina_lg,
        fg_color='#BBBBBB',
        hover_color='#BBBBBB',
        text='Lembrar senha',
        text_color='black',
        checkbox_height=20,
        checkbox_width=20,
        checkmark_color='black',
        bg_color='#F3F3F3'
    )
    lembrar_senha.place(relx=0.4, rely=0.62, anchor="center")

    eye_open_img = ctk.CTkImage(Image.open("images/eye_open.png").resize((20, 20)))
    eye_closed_img = ctk.CTkImage(Image.open("images/eye_closed.png").resize((20, 20)))

    mostrar_senha = [False]

    def alternar_senha():
        """
        Alterna entre mostrar e ocultar o conteúdo do campo de senha.
        """
        if mostrar_senha[0]:
            senha_entrada.configure(show="*")
            olho_botao.configure(image=eye_closed_img)
        else:
            senha_entrada.configure(show="")
            olho_botao.configure(image=eye_open_img)
        mostrar_senha[0] = not mostrar_senha[0]

    olho_botao = ctk.CTkButton(
        master=pagina_lg,
        width=20,
        height=20,
        image=eye_closed_img,
        text="",
        fg_color="#BBBBBB",
        hover_color="grey",
        border_width=0,
        corner_radius=0,
        command=alternar_senha
    )
    olho_botao.place(x=262, y=360)

    entrar_button = ctk.CTkButton(
        master=pagina_lg,
        width=164,
        height=41,
        text='Entrar',
        text_color='Black',
        fg_color='#BBBBBB',
        border_width=1,
        border_color='black',
        hover_color='grey',
        cursor='hand2'
    )
    entrar_button.place(relx=0.5, rely=0.68, anchor="center")

    frame = ctk.CTkFrame(master=pagina_lg, fg_color='#F3F3F3')
    frame.place(relx=0.5, rely=0.74, anchor="center")

    label1 = ctk.CTkLabel(master=frame, text='Não tem uma conta?', text_color='black')
    label1.pack(side="left")

    def abrir_cadastro():
        """
        Fecha a tela de login e abre a tela de cadastro.
        """
        pagina_lg.destroy()
        import cadastro
        cadastro.tela_cadastro()

    label2 = ctk.CTkLabel(
        master=frame,
        text=' Crie aqui.',
        text_color='blue',
        cursor="hand2",
        font=ctk.CTkFont(family="Arial", size=12, underline=True)
    )
    label2.pack(side="left")
    label2.bind("<Button-1>", lambda e: abrir_cadastro())

    pagina_lg.mainloop()
