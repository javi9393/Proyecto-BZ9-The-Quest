import pygame 




from thequest import ALTO, ANCHO
from thequest.pantallas import Titulo, Partida, Puntuaciones


class Juego:
    jugando = 0
    def __init__(self):
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.pantallas = [
            Titulo(self.pantalla),
            Partida(self.pantalla),
            Puntuaciones(self.pantalla)]
        self.jugando = 1

    def jugar(self):
        while self.jugando == 1:
            for escena in self.pantallas:
                escena.bucle_principal()

        
    