from pygame import *

mixer.init()
#mixer.music.load('xzd.mp3')
#mixer.music.play()
font.init()
font = font.Font(None, 50)
perdiste1 = font.render('JUGADOR 1 PERDIO',True,(39, 166, 245))
perdiste2 = font.render('JUGADOR 2 PERDIO',True,(39, 156, 230))
al_v = 500
an_v = 700
sonido_rebote = mixer.Sound('kick.ogg')
fondo_imagen = transform.scale(image.load('a.png'),(an_v,al_v))
fondo = (32, 13, 161 )
ventana = display.set_mode((an_v, al_v ))
ventana.fill(fondo)

class gamesprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x , player_y, size_x , size_y , player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
   
    def reset(self):
        ventana.blit(self.image,(self.rect.x, self.rect.y))

class Player(gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < al_v - 80:
            self.rect.y += self.speed

    def updatea(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < al_v - 80:
            self.rect.y += self.speed
           

pelota = gamesprite('pelota.jpeg', 200, 200 , 50 , 50 , 4)
plataforma1 = Player('pared.jpg', 30, 200 , 50 , 150 , 4)
plataforma2 = Player('pared.jpg', 520, 200 , 50 , 150 , 4)
clock = time.Clock()
FPS = 60
game = True

cambiox = 3
cambioy = 3
finish = False
while game:



    for e in event.get():
        if e.type == QUIT :
            game = False
    if finish != True :
        #ventana.fill(fondo)
        ventana.blit(fondo_imagen,(0,0))                   
        plataforma1.updatea()
        plataforma2.update()
        pelota.update()

        pelota.rect.x += cambiox
        pelota.rect.y += cambioy
        if sprite.collide_rect(pelota, plataforma1) or sprite.collide_rect(plataforma2 , pelota):
            cambiox *= -1
            cambioy *= 1
            sonido_rebote.play()

        if pelota.rect.y > al_v - 50 or pelota.rect.y < 0:
            cambioy *= -1

        if pelota.rect.x < 0:  
            ventana.blit(perdiste1,(200,200))
            finish = True
            game = True
        if  pelota.rect.x > an_v:
            ventana.blit(perdiste2,(200,200))
            finish = True
            game = True
        
        plataforma1.reset()
        plataforma2.reset()
        pelota.reset()
    display.update()
    clock.tick(FPS)