import os
import pygame 

from . import ANCHO, ALTO, FPS
from .objetos import Nave, Objeto, Final, Explosion
import sqlite3
import time


class Pantalla:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()

    def bucle_prinicpal(self):
        pass

class Titulo(Pantalla):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        letra = 20
        separacion = 100
        

        self.logo = pygame.image.load(
            os.path.join('Imagenes', 'TITULO.png')
        )
        self.logo_size = pygame.transform.scale(self.logo, (300, 300))
        self.logo_pos = (300, 50)

        ruta = os.path.join('Fuente_letra', 'ka1.ttf')
        fuente = pygame.font.Font(ruta, letra)
        self.texto_inicio = fuente.render(
            'Pulsa <ESPACIO> para comenzar partida', True, 'white')
        
        self.texto_pos = (
            ANCHO/2 - self.texto_inicio.get_width() / 2,
            ALTO - separacion - self.texto_inicio.get_height()
        )
    def bucle_principal(self):
    
        self.historia = pygame.image.load(
            os.path.join('Imagenes', 'Historia.png')
        )
        self.historia_size = pygame.transform.scale(self.historia, (600, 600))
        self.rect = self.historia.get_rect(
            midbottom=(
            450,
            1200)) 
        
        
        i=0
        Press = 0

        while i < 1000:
            
          
            self.rect.y -= 1
            i += 1
            time.sleep(0.01)
            self.pantalla.fill((0, 0, 0))
            self.pantalla.blit(self.historia_size, self.rect)
            pygame.display.flip()
                    
                      
                        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
            self.pantalla.fill((60, 0, 120))
            
            self.pantalla.blit(self.logo_size, self.logo_pos)

            self.pantalla.blit(self.texto_inicio, self.texto_pos)
            pygame.display.flip()
class Partida(Pantalla):
    vidas = 3
    marcador= 0
    nivel = 1
    puntuacion = 0
    ruta = os.path.join('Fuente_letra', 'ka1.ttf')
    fuente = pygame.font.Font(ruta, 20)
    punt_pos =(50,20)
    vidas_pos =(850,20)
    cambio_nivel=0
    transicion = 0
    terminado = 0
    sonido = (os.path.join('Sonido', 'explosion.wav'))
    nivel_final= 0
   
    
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.jugador = Nave()
        self.obstaculo = Objeto()
        self.obstaculo1 = Objeto()
        self.obstaculo2 = Objeto()
        self.fin = Final()
        self.expo = Explosion()
        pygame.mixer.music.load(self.sonido)
        
        self.jugador.rect.x = 14
        self.jugador.rect.y = 250
        

        
        
    def bucle_principal(self):
        while True:
            self.reloj.tick(FPS)
            self.jugador.rect.x = 14
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if self.obstaculo.rect.x < -100:
                self.marcador += 100
                self.obstaculo = Objeto()
                self.puntuacion += 100
            if self.obstaculo1.rect.x < -100:
                self.marcador += 100
                self.obstaculo1 = Objeto()
                self.puntuacion += 100
            if self.obstaculo2.rect.x < -100:
                self.marcador += 100
                self.obstaculo2 = Objeto()
                self.puntuacion += 100

            self.obstaculo.golpe(self.jugador.rect.y)
            self.obstaculo1.golpe(self.jugador.rect.y)
            self.obstaculo2.golpe(self.jugador.rect.y)

            if  self.obstaculo.bajarvida == 1:
                pygame.mixer.music.play()
                self.expo.Pum(self.jugador.rect.x,self.jugador.rect.y)
                self.pantalla.blit(self.expo.exp, self.expo.rect)
                pygame.display.flip()
                time.sleep(2)
                self.vidas -=1
                self.obstaculo.nuevo_obj()
                self.obstaculo1.nuevo_obj()
                self.obstaculo2.nuevo_obj()
                self.jugador.rect.y = 275
                self.obstaculo.bajarvida = 0

            if  self.obstaculo1.bajarvida == 1:
                pygame.mixer.music.play()
                self.expo.Pum(self.jugador.rect.x,self.jugador.rect.y)  
                self.pantalla.blit(self.expo.exp, self.expo.rect)
                pygame.display.flip()
                time.sleep(2)
                self.vidas -=1
                self.obstaculo.nuevo_obj()
                self.obstaculo1.nuevo_obj()
                self.obstaculo2.nuevo_obj()
                self.jugador.rect.y = 275
                self.obstaculo1.bajarvida = 0

            if  self.obstaculo2.bajarvida == 1:
                pygame.mixer.music.play()
                self.expo.Pum(self.jugador.rect.x,self.jugador.rect.y)
                self.pantalla.blit(self.expo.exp, self.expo.rect)
                pygame.display.flip()
                time.sleep(2)
                self.vidas -=1
                self.obstaculo.nuevo_obj()
                self.obstaculo1.nuevo_obj()
                self.obstaculo2.nuevo_obj()
                self.jugador.rect.y = 275
                self.obstaculo2.bajarvida = 0
            
            if self.marcador>=500:
                self.cambio_nivel = 1
            if self.marcador>=1000:
                self.cambio_nivel = 2
            if self.marcador>=1500:
                self.cambio_nivel = 3

            if self.cambio_nivel == 1 and self.nivel == 1:
                self.transicion = 1
                self.nivel = 2
            if self.cambio_nivel == 2 and self.nivel == 2:
                self.transicion = 1
                self.nivel = 3
            if self.cambio_nivel == 3 and self.nivel == 3:
                self.transicion = 1
                self.nivel_final = 1
                

            if self.transicion == 1:
                self.jugador.vuelta = 1
                self.Retorno()
            
        
            
            if self.vidas == 0:
                print("Gameover")
                self.Juego_acabado()
              
            if self.terminado == 1:
                self.terminado = 0
                return
        


            self.jugador.update()
            self.obstaculo.update()
            self.obstaculo1.update()
            self.obstaculo2.update()
            self.pantalla.fill((0,0,0))
            self.pantalla.blit(self.fin.ffinal_size, self.fin.rect)
            self.pantalla.blit(self.jugador.nave_recta, self.jugador.rect)
            self.pantalla.blit(self.obstaculo.img_obj, self.obstaculo.rect)
            self.pantalla.blit(self.obstaculo1.img_obj, self.obstaculo1.rect)
            self.pantalla.blit(self.obstaculo2.img_obj, self.obstaculo2.rect)
            
            text_marcador = (f"{self.puntuacion}")
            self.texto_marc = self.fuente.render(text_marcador, True, 'white')
            self.pantalla.blit(self.texto_marc, self.punt_pos)
            text_vidas = (f"{self.vidas}")
            self.texto_vidas = self.fuente.render(text_vidas, True, 'white')
            self.pantalla.blit(self.texto_vidas, self.vidas_pos)

            pygame.display.flip()

    def Retorno(self):
        while self.transicion == 1:
            self.reloj.tick(FPS)
            
            self.jugador.vuelta_centro()
            self.jugador.aterrizando()
            #self.jugador.giro_nave() No se sabe que pasa


            self.fin.update()
            self.obstaculo.update()
            self.obstaculo1.update()
            self.obstaculo2.update()
            self.pantalla.fill((0,0,0))
            self.pantalla.blit(self.fin.ffinal_size, self.fin.rect)
            self.pantalla.blit(self.jugador.nave_recta, self.jugador.rect)
            self.pantalla.blit(self.obstaculo.img_obj, self.obstaculo.rect)
            self.pantalla.blit(self.obstaculo1.img_obj, self.obstaculo1.rect)
            self.pantalla.blit(self.obstaculo2.img_obj, self.obstaculo2.rect)

            text_marcador = (f"{self.puntuacion}")
            self.texto_marc = self.fuente.render(text_marcador, True, 'white')
            self.pantalla.blit(self.texto_marc, self.punt_pos)
            text_vidas = (f"{self.vidas}")
            self.texto_vidas = self.fuente.render(text_vidas, True, 'white')
            self.pantalla.blit(self.texto_vidas, self.vidas_pos)

            pygame.display.flip()

    
            if self.jugador.fin_nivel ==1:
                if self.nivel_final == 1:
                    self.transicion = 0
                    self.jugador.fin_nivel = 0
                    self.Felicidades()
                else:
                    self.transicion = 0
                    self.jugador.fin_nivel = 0
                    self.Texto_nivel()
                    
                
    
    def Felicidades(self):
        ruta = os.path.join('Fuente_letra', 'ka1.ttf')
        fuente = pygame.font.Font(ruta, 20)
        fuente1 = pygame.font.Font(ruta, 50)
        self.texto_in = fuente.render(
            'Pulsa <ESPACIO> para finalizar', True, 'white')
        
        self.texto_pos = (
            ANCHO/2 - self.texto_in.get_width() / 2,
            ALTO - 100 - self.texto_in.get_height())
        self.pantalla.fill((0,0,0))
        text_ending = ("Felicidades")
        text_ending1 = ("Has encontrado un luga habitable")
        self.texto_end = fuente1.render(text_ending, True, 'white')
        self.texto_end1 = self.fuente.render(text_ending1, True, 'white')
        self.pantalla.blit(self.texto_end, (
            ANCHO/2 - self.texto_end.get_width() / 2,
            200))
        self.pantalla.blit(self.texto_end1, (
            ANCHO/2 - self.texto_end1.get_width() / 2,
            300))
        self.pantalla.blit(self.texto_in, self.texto_pos)
        self.fin.esconder()
        self.pantalla.blit(self.fin.ffinal_size, self.fin.rect)
        pygame.display.flip()
        
        Bucle = True
        while Bucle ==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    Bucle = False
        self.insertarVariable(self.puntuacion)
        self.nivel_final= 0
        self.terminado = 1
        self.marcador = 0
        self.puntuacion = 0
        self.nivel = 0
        self.terminado = 1
        self.vidas = 3
        
        

    def Texto_nivel(self):
        ruta = os.path.join('Fuente_letra', 'ka1.ttf')
        fuente = pygame.font.Font(ruta, 20)
        self.texto_in = fuente.render(
            'Pulsa <ESPACIO> para seguir', True, 'white')
        
        self.texto_pos = (
            ANCHO/2 - self.texto_in.get_width() / 2,
            ALTO - 200 - self.texto_in.get_height())
        self.pantalla.fill((0,0,0))
        text_nivel = (f"Nivel {self.nivel}")
        self.texto_niv = self.fuente.render(text_nivel, True, 'white')
        self.pantalla.blit(self.texto_niv, (400,300))
        self.pantalla.blit(self.texto_in, self.texto_pos)
        self.fin.esconder()
        self.pantalla.blit(self.fin.ffinal_size, self.fin.rect)
        pygame.display.flip()
        self.obstaculo = Objeto()
        self.obstaculo1 = Objeto() 
        self.obstaculo2 = Objeto()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
        
        
                
        
    
    def Juego_acabado(self):
        
        self.pantalla.fill((0,0,0))
        text_over = ("Game Over")
        self.texto_ov = self.fuente.render(text_over, True, 'white')
        self.pantalla.blit(self.texto_ov, (400,200))
        text_marcador = (f"{self.marcador}")
        self.texto_marc = self.fuente.render(text_marcador, True, 'white')
        self.pantalla.blit(self.texto_marc, (400,300))
        pygame.display.flip()
        self.finish = 1
        time.sleep(5)
        self.pantalla.fill((0,0,0))
        self.insertarVariable(self.puntuacion)
        pygame.display.flip()
        self.marcador = 0
        self.puntuacion = 0
        self.nivel = 0
        self.terminado = 1
        self.vidas = 3
    
    def insertarVariable(self, puntuacion):
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(400, 300, 40, 32)
        color_inactive = pygame.Color('lightskyblue3')
        
        color = color_inactive
        text = ''
        activo = True
        done = False
        sqliteConnection = sqlite3.connect('puntuaciones.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='stocks' ''')
        if  not cursor.fetchone()[0]==1 : {
	        cursor.execute('''CREATE TABLE stocks
               (Name, Puntuacion)''')
        }
        
        ruta = os.path.join('Fuente_letra', 'ka1.ttf')
        fuente = pygame.font.Font(ruta, 20)
        self.texto_in = fuente.render(
            'Introduce nombre del jugador 3 palabras', True, 'white')
        
        self.texto_pos = (
        ANCHO/2 - self.texto_in.get_width() / 2,
        100)
            
        self.pantalla.fill((0, 0, 250))
        self.pantalla.blit(self.texto_in, self.texto_pos)
        pygame.display.flip()
        done = False

        while not done:
                for event in pygame.event.get():
                    
                    if activo == False:
                        done = True

                    if activo == True:
                        if event.type == pygame.KEYDOWN:
                        
                            if event.key == pygame.K_RETURN:
                                print(text)
                                text = ''
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode
                            if len(text)==3:
                                activo = False
                txt_surface = font.render(text, True, color)
                width = max(200, txt_surface.get_width()+10)
                input_box.w = width
                self.pantalla.blit(txt_surface, (405, 305))
                self.pantalla.blit(self.texto_in, self.texto_pos)
                pygame.draw.rect(self.pantalla, color, input_box, 2)
                pygame.display.flip()
        sqlite_insert_with_param = """INSERT INTO stocks
                        (Name,Puntuacion) 
                        VALUES (?, ?);"""

        data_tuple = (text, puntuacion)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")
        
        rows = cursor.execute("SELECT Puntuacion FROM stocks ORDER BY Puntuacion DESC")
        rows = cursor.fetchmany(size= 3)
        punt1 = rows[0]
        punt2 = rows[1]
        punt3 = rows[2]
        rows = cursor.execute("SELECT Name FROM stocks ORDER BY Puntuacion DESC")
        rows = cursor.fetchmany(size= 3)
        texto1 = rows[0]
        texto2 = rows[1]
        texto3 = rows[2]
               

            
        cursor.close()
        Puntuaciones.update(self,texto1,punt1,texto2,punt2,texto3,punt3)
            

        




class Puntuaciones(Pantalla):
    texto1=""
    texto2=""
    texto3=""
    punt1=""
    punt2=""
    punt3=""
    
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join('Fuente_letra', 'ka1.ttf')
        fuente = pygame.font.Font(ruta, 20)
        self.texto_in = fuente.render(
            'Pulsa <ESPACIO> para ir al inicio', True, 'white')
        
        self.texto_pos = (
            ANCHO/2 - self.texto_in.get_width() / 2,
            ALTO - 500 - self.texto_in.get_height())
    
    def update(self,txt1,pu1,txt2,pu2,txt3,pu3):
        self.texto1=txt1
        self.texto2=txt2
        self.texto3=txt3
        self.punt1=pu1
        self.punt2=pu2
        self.punt3=pu3
        
    def bucle_principal(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
            self.texto1_posi = (
            300 ,
            ALTO - 300 )
            self.texto2_posi = (
            300 ,
            ALTO - 250 )
            self.texto3_posi = (
            300 ,
            ALTO - 200 )
            self.pantalla.fill((0, 0, 250))
            self.punt1_posi = (
            400 ,
            ALTO - 300)
            self.punt2_posi = (
            400 ,
            ALTO - 250 )
            self.punt3_posi = (
            400 ,
            ALTO - 200 )
            text1=os.path.join(self.texto1,self.punt1)
            text2=os.path.join(self.texto2,self.punt2)
            text3=os.path.join(self.texto3,self.punt3)
            #print(text1)
            #print(text2)
            #print(text3)
            
            self.pantalla.blit(self.texto_in, self.texto_pos)
            #self.pantalla.blit(text1, self.texto1_posi)
            #self.pantalla.blit(text2, self.texto2_posi)
            #self.pantalla.blit(text3, self.texto3_posi)
            pygame.display.flip()

