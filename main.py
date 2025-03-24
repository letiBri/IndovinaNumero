import flet as ft
from controller import Controller
from view import View

def main(page: ft.Page):
    v = View(page) #creo la view
    c = Controller(v) #creo il controller a cui passo la view
    v.setController(c) #setto nella view il controller come parametro
    v.caricaInterfaccia()

ft.app(target=main)
