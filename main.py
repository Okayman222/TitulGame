import pygame
import math
from random import randint

bullets = pygame.sprite.Group()
monsters = pygame.sprite.Group()

pygame.font.init()
font1 = pygame.font.Font(None, 80)
lose  = font1.render('YOU LOSE', True, (180, 0,0))

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

finish = False

winx = 1940
winy = -20


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
        self.isjump = False
        self.us = 1
        self.storona = 'right'

    def death(self):
        self.kill()

    def move2(self):
        self.rect.x -= self.speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):

    def move4(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

    def move3(self):
        self.rect.x += self.speed
        if self.rect.y > win_width:
            self.kill()

class Hero(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero.rect.x > 5:
            hero.rect.x -= 10
            hero.image = pygame.transform.scale(pygame.image.load('d2.png'), (90, 80))
            self.us = 2

        if keys[pygame.K_RIGHT] and hero.rect.x < win_width - 80:
            hero.rect.x += 10
            hero.image = pygame.transform.scale(pygame.image.load('d.png'), (90, 80))
            self.us = 1

        if not (self.isjump):
            if keys[pygame.K_LEFT] and self.rect.x > 5:
                self.rect.x -= 10
            if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
                self.rect.x += 10
            if keys[pygame.K_UP] :
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

    def fire1(self):
        bullet = Bullet('ullet.png', self.rect.centerx,  self.rect.centery, 15, 20, 15)
        bullet.storona = 'right'
        bullets.add(bullet)

    def fire2(self):
        bullet = Bullet('ullet.png', self.rect.centerx,  self.rect.centery, 15, 20, 15)
        bullet.storona = 'left'
        bullets.add(bullet)



for i in range(2):
    monster = GameSprite('m1.png', 1920, win_height - 85, 70, 90, randint(1,10))
    monsters.add(monster)







hero = Hero('d.png', 20, win_height - 80, 90 ,80 ,4)

game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if hero.us == 1:
                    hero.fire1()
                else:
                    hero.fire2()
    if not finish:


        for i in range(0,col):
            window.blit(bg,(i*bg_width + scroll,0))

        bullets.draw(window)
        monsters.draw(window)

        for i in bullets:
            if i.storona == 'right':
                i.move3()
        for i in bullets:
            if i.storona == 'left':
                i.move4()

        collides = pygame.sprite.groupcollide(monsters, bullets, True, True)
        for i in collides:
            monster = GameSprite('m1.png', 1920, win_height - 85, 70, 90, randint(1, 10))
            monsters.add(monster)



        if pygame.sprite.spritecollide(hero, monsters, False):
            finish = True
            window.blit(lose, (800, win_height / 2))



        scroll -=2

        if scroll*-1 > bg_width:
            scroll = 0

        monster.reset()
        for i in monsters:
            i.move2()
        hero.reset()
        hero.update()

        pygame.display.update()
    clock.tick(FPS)