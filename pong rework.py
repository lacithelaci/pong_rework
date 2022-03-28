import pygame
import random
pygame.init()
pygame.display.set_caption("PONG")

size = (800, 600)

ablak = pygame.display.set_mode(size)

kek = (0, 0, 255)
fekete = (0, 0, 0)
piros = (255, 0, 0)
sarga = (255, 255, 0)
zold = (0, 204, 0)
lila = (255, 51, 255)
szurke=(128,128,128)
r = 30
kx = 300
ky = 300
dx = 5
dy = 5
x = 300
udx = 0
x2 = kx
p1_pont = 0
p2_pont = 0
basic_font = pygame.font.SysFont('Arial', 30)
fps_font = pygame.font.SysFont('Arial', 15)
fpsx= 20
fpsy= 300
clock = pygame.time.Clock()
vege = False
meghalt = False
fpsbeki=False
lehet=0
while not vege:
    fps = random.randint(60, 61)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vege = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                udx = - 5
            if event.key == pygame.K_RIGHT:
                udx = 5
            if event.key == pygame.K_q:
                vege = True
            if event.key == pygame.K_f:
                lehet+=1
                if lehet%2==1:
                    fpsbeki=True
                else:
                    fpsbeki=False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                udx = 0
            if event.key == pygame.K_RIGHT:
                udx = 0

    ablak.fill((fekete))
    uto = pygame.draw.rect(ablak, kek, (x, 560, 200, 30))
    uto2 = pygame.draw.rect(ablak, lila, (x2, 40, 200, 30))
    pygame.draw.circle(ablak, piros, (kx, ky), r)

    kx += dx
    x2 += dx
    ky += dy
    x += udx

    if x < 0:
        x = 0
    if x + 200 > 800:
        x = 600
    if x2 < 0:
        x2 = 0
    if x2 + 200 > 800:
        x2 = 600
    if kx > 800 - r or kx < r:
        dx = - dx
    if ky>600:
        p2_pont+=1
        dy = -dy
        x = 300
        x2 = 300
    if ky<0:
        p1_pont+=1
        dy = -dy
        x = 300
        x2 = 300
    if uto.collidepoint((kx, ky + 20)) and ky > 560 - r:
        dy = - dy
    if uto2.collidepoint((kx, ky - 20)) and ky > 40 + r:
        dy = - dy

    pont1 = basic_font.render(f'{p1_pont}', False, zold)
    ablak.blit(pont1, (780, 560))
    pont2 = basic_font.render(f'{p2_pont}', False, zold)
    ablak.blit(pont2, (780, 20))
    fps_szam = fps_font.render(f'FPS: {fps}', False, szurke)
    if fpsbeki:
        ablak.blit(fps_szam, (fpsx, fpsy))
    pygame.display.flip()
    clock.tick(fps)
