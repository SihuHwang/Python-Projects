import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (0, 255, 17)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('pygame test')
mySound = pygame.mixer.Sound('thunder.ogg')
clock = pygame.time.Clock()

# myFont = pygame.font.SysFont('arial', 30, True, False)
# myFont2 = pygame.font.SysFont('calibri', 50, False, True)
# text_title = myFont.render('Sihu', False, BLACK)
# text_title2 = myFont.render('hi', True, BLACK)

image = pygame.image.load('alert.png')
image = pygame.transform.scale(image, (100,102))
image_width = image.get_rect().size[0]
image_height = image.get_rect().size[1]

imagex = 200
imagey = 300
dx = 0
dy = 0



A_rect = image.get_rect()
B_rect = pygame.Rect(175, 150, 150, 120)

def collision_check(A_rect, B_rect):
    global mySound
    if A_rect.top < B_rect.bottom and B_rect.top < A_rect.bottom and A_rect.left < B_rect.right and B_rect.left < A_rect.right:
       # mySound.play()
        return True
    else:
        return False

playing = True
while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 5
            elif event.key == pygame.K_LEFT:
                    dx = -5
            if event.key == pygame.K_UP:
                dy = -5
            elif event.key == pygame.K_DOWN:
                dy = 5



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_UP:
                dy = 0
            elif event.key == pygame.K_DOWN:
                dy = 0


    B_rect.y = B_rect.y + 5
    if B_rect.top == SCREEN_HEIGHT:
        B_rect.bottom = 0




    A_rect.x += dx
    A_rect.y += dy

    if A_rect.y < 0:
        A_rect.y = 0
    if A_rect.x < 0:
        A_rect.x = 0

    if A_rect.right > SCREEN_WIDTH:
        A_rect.right = SCREEN_WIDTH

    if A_rect.bottom > SCREEN_HEIGHT:
        A_rect.bottom = SCREEN_HEIGHT


    SCREEN.fill(GREEN)


    SCREEN.blit(image, [A_rect.x,A_rect.y])
    pygame.draw.rect(SCREEN, BLACK, B_rect)

    # SCREEN.blit(text_title, (120, dy))
    # SCREEN.blit(text_title2, (120,100))
    collision_check(A_rect, B_rect)
    pygame.display.update()


    if collision_check(A_rect, B_rect):
        mySound.play()
        if A_rect.bottom > B_rect.top and A_rect.top < B_rect.top:
            A_rect.bottom = 152
        elif A_rect.top < B_rect.bottom and A_rect.bottom > B_rect.bottom:
            A_rect.top = 265
        if A_rect.left < B_rect.right and A_rect.right > B_rect.right:
            A_rect.left = 320
        elif A_rect.right > B_rect.left and A_rect.left < B_rect.left:
            A_rect.right = 175



    clock.tick(60)