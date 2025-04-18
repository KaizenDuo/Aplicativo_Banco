import customtkinter as ctk
from PIL import Image, ImageTk

def abrir_app():
    """
    Inicia o aplicativo chamando a tela de login.
    """
    import login
    login.tela_login()

abrir_app()
