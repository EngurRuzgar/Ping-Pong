from logging import PlaceHolder
from pygame import *
from random import randint
from time import \
    time as timer

#Sound and music
mixer.init()
mixer.music.load(PlaceHolder)
mixer.music.play()
pong_sound = mixer.Sound(PlaceHolder)

#Text
font.init()
font1 = font.Font(None, 80)
win1 = font1.render('Player 1 Wins.', True, (34, 139, 34)) #Yeşil
win2 = font1.render('Player 2 Wins.', True, (34, 139, 34)) #Yeşil
font2 = font.Font(None, 36)

#Images
img_back = PlaceHolder #Background
img_player1 = "player1.png" #player 2
img_player2 = "player2.png" #Player 1
img_bullet = "ball.png" #Ball
img_enemy = PlaceHolder #Placeholder
img_ast = PlaceHolder #Placeholder

background = transform.scale(image.load(img_back),(win_width,win_height))

#Sprite Sınıfı
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

#Kahraman (ana oyuncu) Sınıfı
class Player(GameSprite):
    #Ok tuşları ile kontrol sağlama
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

#sprite oluştuduk
player = Player(img_player1, 5, win_height - 100, 80, 100, 10)

#Kahraman (ana oyuncu) Sınıfı
class Player2(GameSprite):
    #Ok tuşları ile kontrol sağlama
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    #Atış yöntemi
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top,15,20,-15)
        bullets.add(bullet)

#sprite oluştuduk
player2 = Player2(img_player2, 5, win_height - 100, 80, 100, 10)


#Mermi sınıfı
class ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        #Ekranın üst kısmına ulaşan mermileri yok etme
        if self.rect.y < 0:
            self.kill()

#Pencere oluşturuyorum
win_width = 700
win_height = 500
display.set_caption("pingy pongy")
window = display.set_mode((win_width,win_height))


