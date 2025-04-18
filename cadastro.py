import customtkinter as ctk
from PIL import Image, ImageTk

def tela_cadastro():
    """
    Cria e exibe a interface gráfica da tela de cadastro de usuário.

    Inclui campos para:
    - Usuário, senha e confirmação de senha.
    - Botões para mostrar/ocultar senhas.
    - Botão de cadastro.
    - Link para voltar à tela de login.

    Returns:
        None
    """
    pagina_cd = ctk.CTk()
    pagina_cd.geometry("375x667")
    pagina_cd.title("Cadastro")
    pagina_cd.resizable(False, False)
    pagina_cd.iconbitmap("images/icon.ico")

    fundo_imagem = Image.open("images/cadastro.png")
    fundo_imagem = ctk.CTkImage(light_image=fundo_imagem, size=(375, 667))
    
    fundo_label = ctk.CTkLabel(master=pagina_cd, image=fundo_imagem)
    fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

    usuario_entrada = ctk.CTkEntry(
        master=pagina_cd,
        placeholder_text='Usuário',
        placeholder_text_color='black',
        fg_color='#BBBBBB',
        text_color='black',
        width=208,
        height=33
    )
    usuario_entrada.place(relx=0.5, rely=0.44, anchor="center")

    senha_entrada = ctk.CTkEntry(
        master=pagina_cd,
        placeholder_text='Senha',
        placeholder_text_color='black',
        fg_color='#BBBBBB',
        text_color='black',
        show="*",
        width=208,
        height=33
    )
    senha_entrada.place(relx=0.5, rely=0.52, anchor="center")

    confirmar_senha_entrada = ctk.CTkEntry(
        master=pagina_cd,
        placeholder_text='Confirmar Senha',
        placeholder_text_color='black',
        fg_color='#BBBBBB',
        text_color='black',
        show="*",
        width=208,
        height=33
    )
    confirmar_senha_entrada.place(relx=0.5, rely=0.60, anchor="center")

    eye_open_img = ctk.CTkImage(Image.open("images/eye_open.png").resize((20, 20)))
    eye_closed_img = ctk.CTkImage(Image.open("images/eye_closed.png").resize((20, 20)))

    mostrar_senha = [False]
    mostrar_senha2 = [False]

    def alternar_senha():
        """Alterna a visibilidade do campo de senha principal."""
        if mostrar_senha[0]:
            senha_entrada.configure(show="*")
            olho_botao.configure(image=eye_closed_img)
        else:
            senha_entrada.configure(show="")
            olho_botao.configure(image=eye_open_img)
        mostrar_senha[0] = not mostrar_senha[0]

    def alternar_confsenha():
        """Alterna a visibilidade do campo de confirmação de senha."""
        if mostrar_senha2[0]:
            confirmar_senha_entrada.configure(show="*")
            olho_botao2.configure(image=eye_closed_img)
        else:
            confirmar_senha_entrada.configure(show="")
            olho_botao2.configure(image=eye_open_img)
        mostrar_senha2[0] = not mostrar_senha2[0]

    olho_botao = ctk.CTkButton(
        master=pagina_cd,
        image=eye_closed_img,
        width=20,
        height=20,
        text="",
        fg_color="#BBBBBB",
        hover_color="grey",
        border_width=0,
        corner_radius=0,
        command=alternar_senha
    )
    olho_botao.place(x=262, y=333)

    olho_botao2 = ctk.CTkButton(
        master=pagina_cd,
        image=eye_closed_img,
        width=20,
        height=20,
        text="",
        fg_color="#BBBBBB",
        hover_color="grey",
        border_width=0,
        corner_radius=0,
        command=alternar_confsenha
    )
    olho_botao2.place(x=262, y=386)

    def cadastrar_usuario():
        """
        Valida as informações de cadastro e exibe mensagens na interface.

        Verifica se o campo de usuário e as senhas foram inseridos corretamente,
        se as senhas coincidem e exibe mensagens de erro ou sucesso no rótulo `resultado_login`.
        """
        usuario = usuario_entrada.get()
        senha = senha_entrada.get()
        confirmar_senha = confirmar_senha_entrada.get()

        if usuario == "":
            resultado_login.configure(text="O usuário não foi inserido!",
                                    text_color="#FF0000")
        elif senha == "":
            resultado_login.configure(text="A senha não foi inserida!",
                                    text_color="#FF0000")
        elif senha != confirmar_senha:
            resultado_login.configure(text="As senhas não coincidem!",
                                    text_color="#FF0000")
        else:
            resultado_login.configure(text="Cadastro feito com sucesso!",
                                    text_color="#008000")
            print(f"Usuário: {usuario}, Senha: {senha}")

    botao_cadastro = ctk.CTkButton(
        master=pagina_cd,
        width=164,
        height=41,
        text="Cadastrar",
        text_color='Black',
        fg_color='#BBBBBB',
        border_width=1,
        border_color='black',
        hover_color='grey',
        cursor='hand2',
        command=cadastrar_usuario
    )
    botao_cadastro.place(relx=0.5, rely=0.71, anchor="center")

    frame = ctk.CTkFrame(master=pagina_cd, fg_color='#F3F3F3')
    frame.place(relx=0.5, rely=0.77, anchor="center")

    label1 = ctk.CTkLabel(master=frame, text='Já tem uma conta?', text_color='black')
    label1.pack(side="left")

    def abrir_login():
        """Fecha a tela de cadastro e abre a tela de login."""
        pagina_cd.destroy()
        import login
        login.tela_login()

    label2 = ctk.CTkLabel(
        master=frame,
        text=' Entre aqui.',
        text_color='blue',
        cursor="hand2",
        font=ctk.CTkFont(family="Arial", size=12, underline=True)
    )
    label2.pack(side="left")
    label2.bind("<Button-1>", lambda e: abrir_login())

    resultado_login = ctk.CTkLabel(
        master=pagina_cd,
        fg_color='#F3F3F3',
        text="  ",
        font=ctk.CTkFont(family="Arial", size=12),
    )
    resultado_login.place(relx=0.5, y=440, anchor="center")

    pagina_cd.mainloop()
