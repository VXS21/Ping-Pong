from pygame import *

from random import *

win_width=700  
win_height = 500  
window = display.set_mode((win_width, win_height))#создай окно игры

clock = time.Clock()
FPS = 60
font.init()
font1 = font.Font(None, 75)
win1 = font1.render('PLAYER 1 WIN!' , True , (0, 255, 0))
lose1 = font1.render('PLAYER 1 LOSE!' , True , (255, 0, 0))

font2 = font.Font(None, 75)
win2 = font2.render('PLAYER 2 WIN!' , True , (0, 255, 0))
lose2 = font2.render('PLAYER 2 LOSE!' , True , (255, 0, 0))


speed = 15

speed_x = 3

speed_y = 3

background = transform.scale(image.load('ФОНДЛЯПИНПОНГА.jpg'), (700, 500))

display.set_caption('Пинг-понг') 


lost = 0
check = 0 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, sizeX, sizeY, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizeX,sizeY))
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
                self.rect.y += self.speed
    def move2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
                self.rect.y += self.speed

class Enemy(GameSprite):
    def play21(self):
        direction = 'left'
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:  
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed 
        if self.direction == 'right':
            self.rect.x += self.speed
            
ball = GameSprite('penis_ball.png', 350,250,50, 50, 10)

racketka1 = Player('racket.png', 20, 50, 30, 100, 15) 

racketka2 = Player('racket.png', 650, 50, 30, 100, 15) 


enemy_list = {}

for enemy in enemy_list:
    enemy.update()



finish = False
game = True

while game:

    window.blit(background,(0, 0))

    for e in event.get():
            if e.type == QUIT:
                game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(racketka1, ball) or sprite.collide_rect(racketka2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (150, 200))


    if ball.rect.x > 670:
        finish = True
        window.blit(lose2, (150, 200))


    racketka1.reset()
    racketka1.move()
    racketka2.reset()
    racketka2.move2()

    ball.reset()    
                

        
    display.update()
    clock.tick(FPS)
