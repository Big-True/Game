import pygame
import random
pygame.init()
logo = pygame.image.load(r'./res/1.jpg')
pygame.display.set_icon(logo)
pygame.display.set_caption('东方大瞎眼')
screen = pygame.display.set_mode((800, 600))
images = list([pygame.transform.scale(pygame.image.load(
    r'./res/%d.jpg' % m), (50, 50)) for m in range(1, 21)])
map = list([[-1 if int((m+n*16) % 50/2)+1>20 else int((m+n*16) % 50/2)+1 for m in range(16)] for n in range(12)])
for a in range(1000):
    i = [random.randint(0, 11), random.randint(0, 15)]
    j = [random.randint(0, 11), random.randint(0, 15)]
    map[i[0]][i[1]], map[j[0]][j[1]] = map[j[0]][j[1]], map[i[0]][i[1]]
print(map)
while True:
    screen.fill((255, 255, 255))
    for i in range(0, 16):
        for j in range(0, 12):
            if map[j][i] >= 0:
                screen.blit(images[map[j][i]-1], (i*50, j*50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
