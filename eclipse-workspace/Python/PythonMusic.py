import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800


pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.mixer.music.load('bagroundsample.mp3')
mySound = pygame.mixer.Sound('thunder.ogg')
pygame.mixer.music.play(-1)



playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mySound.play()
            elif event.key == pygame.K_s:
                mySound.stop()
            elif event.key == pygame.K_UP:
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v + 0.1)
            elif event.key == pygame.K_DOWN:
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v - 0.1)
            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_RIGHT:
                pygame.mixer.music.unpause()




    clock.tick(60)



























































