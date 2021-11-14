from thequest import ANCHO, ALTO
from thequest.TheQuest import Juego


if __name__ == '__main__':
    print("main: main.py")
    print(f'Estoy jugando a {ANCHO}x{ALTO}')
    juego = Juego()
    juego.jugar()