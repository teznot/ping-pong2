from pygame import *

window = display.set_mode((700,500))
windo = display.set_caption('Пинг-понг')
window.fill((0, 162, 255))
clock = time.Clock()

#ball = transform.scale(image.load('tenis_ball.png'),(60, 60))
#racket1 = transform.scale(image.load('racket.png'),(50, 150))
#racket2 = transform.scale(image.load('racket.png'),(50, 150))
font.init()
text = font.SysFont('Arial', 40)
lose_l = text.render('Игрок слева проиграл', True, (255, 255, 255))
lose_r = text.render('Игрок справа проиграл', True, (255, 255, 255))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_width,player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed 
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

racket1 = Player('racket.png', 10, 10, 5, 50, 150)
racket2 = Player('racket.png', 640, 340, 5, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 250, 3, 60, 60)
speed_x = 3
speed_y = 3

game = True
finish = False
while game:
    if finish != True:
        window.fill((0, 162, 255))
        if finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if ball.rect.y > 500 - 60 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(lose_l, (200, 200))
            finish = True
        if ball.rect.x > 700 - 60:
            window.blit(lose_r, (200, 200))
            finish = True
        ball.reset()
        racket1.reset()
        racket2.reset()
        racket1.update_l()
        racket2.update_r()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)