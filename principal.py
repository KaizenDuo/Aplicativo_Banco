import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")

def tela_principal():
    '''
    Cria e exibe a interface gráfica da tela principal do aplicativo.
    '''
    pagina_pr = ctk.CTk()
    pagina_pr.geometry("375x667")
    pagina_pr.title("Principal")
    pagina_pr.resizable(False, False)
    pagina_pr.iconbitmap("images/icon.ico")

    pagina_pr.mainloop()

tela_principal()