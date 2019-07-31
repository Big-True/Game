import pygame
import random
pygame.init()
logo = pygame.image.load(r'./res/1.jpg')
pygame.display.set_icon(logo)
pygame.display.set_caption('东方大瞎眼')
clock=pygame.time.Clock()
size = 100
screen = pygame.display.set_mode((800, 600))
images = list([pygame.transform.scale(pygame.image.load(
    r'./res/%d.jpg' % m), (size, size)) for m in range(1, 21)])
map = []


def resize():
    size = size/2


def newgame():
    map[:] = list([[-1 if m+n*(800/size)>(480000/size/size/3*2) else int(((m+n*(800/size)) %
                                                                       40)/2)+1 for m in range(int(800/size))] for n in range(int(600/size))])
    for a in range(int(100000/size)):
        i = [random.randint(0, (600/size)-1), random.randint(0, (800/size)-1)]
        j = [random.randint(0, (600/size)-1), random.randint(0, (800/size)-1)]
        map[i[0]][i[1]], map[j[0]][j[1]] = map[j[0]][j[1]], map[i[0]][i[1]]


newgame()
while True:
    clock.tick(60)
    screen.fill((255, 255, 255))
    temp=0
    for i in range(0, int(800/size)):
        for j in range(0, int(600/size)):
            if map[j][i] >= 0:
                screen.blit(images[map[j][i]-1], (i*size, j*size))
                temp=temp+1
    if temp==0:
        resize()
        newgame()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
