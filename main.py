import pygame
import math
import time

bullets = pygame.sprite.Group()

us = 1

camera_x = 0
camera_y = 0

win_width =1900
win_height = 700

window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('Game')
bg = pygame.image.load('stena.png').convert()
bg_width = bg.get_width()
clock = pygame.time.Clock()
FPS = 60

col = math.ceil(win_width / bg_width) + 1






scroll = 0


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.jump = 10
        self.list = ['d.png','d2.png']
        self.isjump = False
        self.us = 1


    def move2(self):
        self.rect.x -= 1

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):
    def move4(self):
        self.rect.x -= self.speed

    def move3(self):
        self.rect.x += self.speed

class Hero(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero.rect.x > 5:
            hero.rect.x -= 10
            hero.image = pygame.transform.scale(pygame.image.load('d2.png'), (150, 100))
            self.us = 2

        if keys[pygame.K_RIGHT] and hero.rect.x < win_width - 80:
            hero.rect.x += 10
            hero.image = pygame.transform.scale(pygame.image.load('d.png'), (150, 100))
            self.us = 1
        if not (self.isjump):
            if keys[pygame.K_LEFT] and self.rect.x > 5:
                self.rect.x -= 10
            if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
                self.rect.x += 10
            if keys[pygame.K_UP]:
                self.isjump = True
        else:
            if not (self.isjump):
                if keys[pygame.K_LEFT] and self.rect.x > 5:
                    self.rect.x -= 10
                if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
                    self.rect.x += 10
                if keys[pygame.K_UP]:
                    self.isjump = True
            else:
                if self.jump >= -10:
                    if self.jump <= 0:
                        self.rect.y += (self.jump ** 2) / 2

                    else:
                        self.rect.y -= (self.jump ** 2) / 2
                    self.jump -= 1
                else:
                    self.isjump = False
                    self.jump = 10

    def fire(self):
        bullet = Bullet('ullet.png', self.rect.centerx,  self.rect.centery, 15, 20, 15)
        bullets.add(bullet)


monster = GameSprite('m1.png',1920, win_height - 85, 70 ,90 ,4)
hero = Hero('d.png', 20, win_height - 101, 150 ,100 ,4)

game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                hero.fire()



    for i in range(0,col):
        window.blit(bg,(i*bg_width + scroll,0))

    bullets.draw(window)
    if hero.us == 2:
        for i in bullets:
            i.move4()
    elif hero.us == 1:
        for i in bullets:
            i.move3()



    scroll -=2

    if scroll*-1 > bg_width:
        scroll = 0

    monster.reset()
    monster.move2()
    hero.reset()
    hero.update()

    pygame.display.update()
    clock.tick(FPS)