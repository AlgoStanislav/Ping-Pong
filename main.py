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
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        direction_x = 1 if randint(0, 1) == 1 else -1
        direction_y = 1 if randint(0, 1) == 1 else -1
        
        self.speed_x = player_speed * direction_x
        self.speed_y = player_speed * direction_y
        self.coef_x = 1
        self.coef_y = 1
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def switch_x(self):
        self.speed_x *= -1
        self.coef_x += 0.05
        self.speed_x *= self.coef_x
    def switch_y(self):
        self.speed_y *= -1
        self.coef_y += 0.03
        self.speed_y *= self.coef_y

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
ball = Ball("ball.png", randint(200, win_w - 200), randint(200, win_h - 200), 50, 50 , 4)

font.init()
font_text = font.Font(None, 72)
win_left_text = font_text.render("WIN LEFT!", 1, (0, 255, 0))
win_right_text = font_text.render("WIN RIGHT!", 1, (0, 255, 0))
result_text = win_left_text

clock = time.Clock()
FPS = 60
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        player_left.update_l()
        player_right.update_r()
        ball.update()

        if ball.rect.y < 0 or ball.rect.y > win_h - ball.image.get_height():
            ball.switch_y()
        
        if sprite.collide_rect(ball, player_left) or sprite.collide_rect(ball, player_right):
            ball.switch_x()
        
        if ball.rect.x < 0:
            result_text = win_right_text
            finish = True
        
        if ball.rect.x > win_w - ball.image.get_width():
            result_text = win_left_text
            finish = True

        window.blit(background, (0, 0))
        player_left.reset()
        player_right.reset()
        ball.reset()
    else:
        window.blit(result_text, (200, win_h / 2 - 40))

    display.update()
    clock.tick(FPS)