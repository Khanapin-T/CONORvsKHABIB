from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг понг')
background = transform.scale(image.load('background_pp.png'), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__(player_image, player_x, player_y, player_speed, size_x, size_y)
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 345:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed                                                                                                   

platform_l = Player('platform_left.png', 10, 250, 5, 20, 140)
platform_r = Player('platform_right.png', 670, 250, 5, 20, 140)
ball = GameSprite('ball.png', 200, 200, 4, 30, 30)

mixer.init()
mixer.music.load('music_pp.ogg')
mixer.music.set_volume(0.6)
mixer.music.play()

fps = 60
clock = time.Clock()

speed_x = 4
speed_y = 4

game = True
finish = False

font.init()
font = font.Font(None, 70)
p1_win = font.render('Конор win!', True, (0, 255, 0))
p2_win = font.render('Хабиб win!', True, (0, 255, 0))

win_sound = mixer.Sound('pobeda.ogg')
win_sound.set_volume(0.4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background, (0, 0))
        platform_l.update_l()
        platform_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        platform_l.reset()
        platform_r.reset()
        ball.reset()

        if sprite.collide_rect(platform_l, ball) or sprite.collide_rect(platform_r, ball):
            speed_x *= -1
            speed_y *= 1
                                                              
        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(p1_win, (200, 200))
            mixer.music.stop()
            win_sound.play()

        if ball.rect.x > win_width:
            finish = True
            window.blit(p2_win, (200, 200))
            mixer.music.stop()
            win_sound.play()

        display.update()
    clock.tick(fps)