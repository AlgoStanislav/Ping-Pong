from pygame import *
from random import randint, random

#48 130
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_h - 135:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_h - 135:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_h:
            self.rect.y = randint(-65, 0)
            self.rect.x = randint(20, win_w - 20)

win_w = 700
win_h = 500

window = display.set_mode((win_w, win_h))

display.set_caption("Ping-Pong")

background = transform.scale(
    image.load("background.jpg"),
    (win_w, win_h)
)

player_left = Player("racket.png", 30, 10, 48, 130, 10)
player_right = Player("racket.png", win_w - 30 - 48 , win_h - 10 - 130, 48, 130, 10)

clock = time.Clock()
FPS = 60
run = True
finish = False

ball = GameSprite("ball.png", win_w / 2, win_h / 2, 50, 50 , 0)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        player_left.update_l()
        player_right.update_r()

        window.blit(background, (0, 0))
        player_left.reset()
        player_right.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)