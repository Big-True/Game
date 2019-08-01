import pygame
import random
pygame.init()
logo = pygame.image.load(r'./res/1.jpg')
pygame.display.set_icon(logo)
pygame.display.set_caption('东方大瞎眼')
clock = pygame.time.Clock()
size = 100
screen = pygame.display.set_mode((800, 600))
images = list([pygame.transform.scale(pygame.image.load(
    r'./res/%d.jpg' % m), (size, size)) for m in range(1, 21)])
map = []


def resize():
    global size
    global images
    size = int(size/2)
    images = list([pygame.transform.scale(pygame.image.load(
        r'./res/%d.jpg' % m), (size, size)) for m in range(1, 21)])


def newgame():
    global map
    if size > 50:
        map = list([[-1 if n > (600/size/2) else int(((m+n*(800/size)) % 10)/2) +
                     1 for m in range(int(800/size))] for n in range(int(600/size))])
    elif size > 25:
        map = list([[-1 if n > (600/size/2) else int(((m+n*(800/size)) % 20)/2) +
                     1 for m in range(int(800/size))] for n in range(int(600/size))])
    else:
        map = list([[-1 if n > (600/size/2) else int(((m+n*(800/size)) % 40)/2) +
                     1 for m in range(int(800/size))] for n in range(int(600/size))])
    for a in range(pow(int(1000/size),2)):
        i = [random.randint(0, int(600/size)-1), random.randint(0, int(800/size)-1)]
        j = [random.randint(0, int(600/size)-1), random.randint(0, int(800/size)-1)]
        map[i[0]][i[1]], map[j[0]][j[1]] = map[j[0]][j[1]], map[i[0]][i[1]]


def check(x, y):
    if map[y][x] == -1:
        p = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        for i in range(y-1, -1, -1):
            if p[0] == [-1, -1, -1]:
                if map[i][x] != -1:
                    p[0] = [x, i, map[i][x]]
        for j in range(x+1, int(800/size)):
            if p[1] == [-1, -1, -1]:
                if map[y][j] != -1:
                    p[1] = [j, y, map[y][j]]
        for j in range(x-1, -1, -1):
            if p[2] == [-1, -1, -1]:
                if map[y][j] != -1:
                    p[2] = [j, y, map[y][j]]
        for i in range(y+1, int(600/size)):
            if p[3] == [-1, -1, -1]:
                if map[i][x] != -1:
                    p[3] = [x, i, map[i][x]]
        if p[0][2] != -1 and p[1][2] != -1 and p[0][2] == p[1][2]:
            map[p[0][1]][p[0][0]] = -1
            map[p[1][1]][p[1][0]] = -1
            p[0] = [-1, -1, -1]
            p[1] = [-1, -1, -1]
        if p[0][2] != -1 and p[2][2] != -1 and p[0][2] == p[2][2]:
            map[p[0][1]][p[0][0]] = -1
            map[p[2][1]][p[2][0]] = -1
            p[0] = [-1, -1, -1]
            p[2] = [-1, -1, -1]
        if p[0][2] != -1 and p[3][2] != -1 and p[0][2] == p[3][2]:
            map[p[0][1]][p[0][0]] = -1
            map[p[3][1]][p[3][0]] = -1
            p[0] = [-1, -1, -1]
            p[3] = [-1, -1, -1]
        if p[2][2] != -1 and p[1][2] != -1 and p[2][2] == p[1][2]:
            map[p[2][1]][p[2][0]] = -1
            map[p[1][1]][p[1][0]] = -1
            p[2] = [-1, -1, -1]
            p[1] = [-1, -1, -1]
        if p[3][2] != -1 and p[1][2] != - 1 and p[3][2] == p[1][2]:
            map[p[3][1]][p[3][0]] = -1
            map[p[1][1]][p[1][0]] = -1
            p[0] = [-1, -1, -1]
            p[1] = [-1, -1, -1]
        if p[2][2] != -1 and p[3][2] != - 1 and p[2][2] == p[3][2]:
            map[p[2][1]][p[2][0]] = -1
            map[p[3][1]][p[3][0]] = -1
            p[2] = [-1, -1, -1]
            p[3] = [-1, -1, -1]


newgame()
while True:
    clock.tick(60)
    screen.fill((255, 255, 255))
    temp = 0
    for i in range(0, int(800/size)):
        for j in range(0, int(600/size)):
            if map[j][i] >= 0:
                screen.blit(images[map[j][i]-1], (i*size, j*size))
                temp = temp+1
    if temp == 0:
        resize()
        newgame()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            check(int(x/size), int(y/size))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                newgame()
            if event.key == pygame.K_n:
                resize()
                newgame()
    pygame.display.flip()
