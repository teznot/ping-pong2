from pygame import *

window = display.set_mode((700,500))
windo = display.set_caption('Пинг-понг')
window.fill((0, 162, 255))

ball = transform.scale(image.load('tenis_ball.png'),(60, 60))
racket1 = transform.scale(image.load('racket.png'),(50, 150))
racket2 = transform.scale(image.load('racket.png'),(50, 150))

game = True
while game:
    window.blit(ball, (200, 250))
    window.blit(racket1, (10, 10))
    window.blit(racket2, (640, 340))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()