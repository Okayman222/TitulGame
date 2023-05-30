import pygame
import math

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


isjump = False
jump = 10

scroll = 0


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y



    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += 10

        if not (isjump):
            if keys[pygame.K_LEFT] and self.rect.x > 5:
                self.rect.x -= 10

            if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
                self.rect.x += 10
            if keys[pygame.K_SPACE]:
                if jump >= -10:
                    if jump < 0:
                        self.rect.y += (jump ** 2) / 4
                    else:
                        self.rect.y -= (jump ** 2) / 4
                    jump -= 1
                else:
                    isjumps = True
                    jump = 10





hero = GameSprite('d.png', 20, win_height - 100, 150 ,100 ,4)

game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    for i in range(0,col):
        window.blit(bg,(i*bg_width + scroll,0))

    scroll -= 1

    if scroll*-1 > bg_width:
        scroll = 0

    hero.reset()
    hero.update()

    pygame.display.update()
    clock.tick(FPS)