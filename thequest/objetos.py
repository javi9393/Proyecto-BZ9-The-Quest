import os
from typing import Iterable
import pygame 
from pygame.sprite import Sprite
import random

from . import ALTO, ANCHO, FPS

class Nave (Sprite):
    vidas = 3
    vivo = True
    velocidad = 1
    iteracion = 0
    fps_animacion = 12
    ancho= 50
    vuelta = 0
    giro = 0
    aterrizar = 0
    angulo = 0
    fin_nivel = 0
    limite_iteracion = FPS/fps_animacion
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
                    'Imagenes', 'nave.png')
            )          
        self.nave = pygame.transform.rotate(self.image, -90)
        self.nave_recta = pygame.transform.scale(self.nave, (50,50))
        self.nave_recta = pygame.transform.scale(self.nave_recta, (50,50))
        self.nave_recta = pygame.transform.scale(self.nave_recta, (50,50))

        self.rect = self.image.get_rect(
        midbottom=(270, ALTO/2))

      

    def update(self, *args, **kwargs):
        
        tecla = pygame.key.get_pressed()
        tecla_pulsada = pygame.key.get_pressed()

        if tecla_pulsada[pygame.K_UP] or tecla_pulsada[pygame.K_DOWN]:
            self.velocidad += 0.1
        else:
            self.velocidad = 1
        
        if self.velocidad > 6:
            self.velocidad = 6

        if tecla[pygame.K_UP]:
            if self.rect.y > 0:
                self.rect.y -= self.velocidad
            if self.rect.y < 0:
                self.rect.y = 0

        if tecla[pygame.K_DOWN]:
            if self.rect.y < ALTO-50:
                self.rect.y += self.velocidad
            if self.rect.y > ALTO-50:
                self.rect.y = ALTO-50

    def vuelta_centro(self):
        if self.rect.y >275:
            self.rect.y -= 1
        if self.rect.y <275:
            self.rect.y +=1
        if self.rect.y == 275:
            self.aterrizar = 1
            self.vuelta = 0

    def giro_nave(self):
        if self.giro == 1:
            if self.angulo <180:
                print(f"entro: {self.angulo}")
                self.angulo += 1
                self.nave_recta = pygame.transform.rotate(self.nave_recta, 1)
        if self.angulo == 180:
            self.giro = 0
    
    def aterrizando(self):
        if self.aterrizar == 1:
            if self.rect.x < 750:
                self.rect.x += 1
            if self.rect.x == 750:
                self.giro = 1
                self.fin_nivel = 1


class Objeto(Sprite):
    nivel = 1
    objetos = 5
    bajarvida = 0
    def __init__(self):
        super().__init__()
        self.nuevo_obj()
        

    def nuevo_obj(self):
        obj = random.randint(0,1)
        rand = random.randint(50,550)
        rand_esc = random.randint(50,100)
        if obj == 0:
            self.image = pygame.image.load(os.path.join(
                    'Imagenes', 'asteroide.png')
            )
        if obj == 1:
            self.image = pygame.image.load(os.path.join(
                    'Imagenes', 'meteorito.png')
            )
        
        self.img_obj = pygame.transform.scale(self.image, (rand_esc, rand_esc))
        self.rect = self.img_obj.get_rect(
            midbottom=(850, rand))
        if self.nivel == 1:
            self.velocidad_objeto = random.randint(2,4)
        if self.nivel == 2:
            self.velocidad_objeto = random.randint(3,5)
        if self.nivel == 3:
            self.velocidad_objeto = random.randint(4,6)
            
    
    def update(self):
        self.rect.x -= self.velocidad_objeto
    

    
    def golpe(self,nave):
        if self.rect.colliderect(14,nave,50,50):
            self.bajarvida = 1
        
class Final(Sprite):

    def __init__(self):
        super().__init__()
        self.final()

    def final(self):  
        self.final = pygame.image.load(
            os.path.join('Imagenes', 'final.png'))
        self.final_size = pygame.transform.scale(self.final,(600,300))
        self.ffinal_size = pygame.transform.rotate(self.final_size, 90)
        self.rect = self.ffinal_size.get_rect(
            midbottom=(900, 600)) 
        self.rect.x = 900
    def update(self):
        if self.rect.x >600:
            self.rect.x -= 1
    def esconder(self):
        self.rect.x = 900

class Explosion(Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
                    'Imagenes', 'explosion.png')
            )          
        self.exp = pygame.transform.scale(self.image, (50,50))
        self.rect = self.exp.get_rect(
            midbottom=(-500, -500))
        

    def Pum(self,X,Y):  
        self.rect.x = X
        self.rect.y = Y
    def NoPum(self):
        self.rect.x = -500
        self.recy.y = -500
