import pygame
import random
import sys

GRAY = (150,150,150)
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 800

DIRCARS = "cars/"
DIRSOUND = "sound/"

STAGE = 1
CAR_COUNT = 5

CARS = []

class Car:
    car_image = ['Car01.png', 'Car02.png', 'Car03.png', 'Car04.png', 'Car05.png', \
                 'Car06.png', 'Car07.png', 'Car08.png', 'Car09.png', 'Car10.png', \
                 'Car11.png', 'Car12.png', 'Car13.png', 'Car14.png', 'Car15.png', \
                 'Car16.png', 'Car17.png', 'Car18.png', 'Car19.png', 'Car20.png', \
                 'Car21.png', 'Car22.png', 'Car23.png', 'Car24.png', 'Car25.png', \
                 'Car26.png', 'Car27.png', 'Car28.png', 'Car29.png', 'Car30.png', \
                 'Car31.png', 'Car32.png', 'Car33.png', 'Car34.png', 'Car35.png', \
                 'Car36.png', 'Car37.png', 'Car38.png', 'Car39.png', 'Car40.png' ]
    def __init__(self, x=0 ,y=0,dx=0,dy=0):
        self.image = ""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rect =''

    def load_car(self, p = ''):
        if p =='p':
            self.image = pygame.image.load(DIRCARS + 'player.png')
            self.image = pygame.transform.scale(self.image, (40, 102))
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            self.image = pygame.image.load(DIRCARS + random.choice(self.car_image))
            self.rect = self.image.get_rect()

            if self.rect.width <= 55:
                carwidth = self.rect.width - 15
                carheight = round((self.rect.height * carwidth)/ self.rect.width)
            else:
                carwidth = self.rect.width
                carheight = self .rect.height

            self.image = pygame.transform.scale(self.image, (carwidth,carheight))
            self.rect.width = carwidth
            self.rect.height = carheight

            self.rect.x = random.randrange(0, WINDOW_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150,-50)

            speed = STAGE + 15
            if speed > 15:
                speed = 15
            self.dy = random.randint(5, speed)

    def draw_car(self):
        SCREEN.blit(self.image, [self.rect.x, self.rect.y])

    def move_x(self):
        self.rect.x += self.dx

    def move_y(self):
        self.rect.y += self.dy

    def check_screen(self):
        if self.rect.right > WINDOW_WIDTH or self.rect.x < 0:
            self.rect.x -= self.dx
        if self.rect.bottom > WINDOW_HEIGHT or self.rect.y < 0:
            self.rect.y -+ self.dy

    def check_collision(self, car, distance = 0):
        if (self.rect.top + distance < car.rect.bottom) \
                and (car.rect.top < self.rect.bottom - distance) \
            and (self.rect.left + distance < car.rect.right) \
                and (car.rect.left < self.rect.right - distance):
            return True
        else:
            return False
def main():
    global SCREEN, CAR_COUNT, WINDOW_HEIGHT, WINDOW_WIDTH

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
                            pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    pygame.display.set_caption('Racing Car Game')
    windowicon = pygame.image.load(DIRCARS + 'icon.png').convert_alpha()
    pygame.display.set_icon(windowicon)

    clock = pygame.time.Clock()

    player = Car(round(WINDOW_WIDTH/2), round(WINDOW_HEIGHT - 150), 0,0)
    player.load_car('p')



    for i in range(CAR_COUNT):
        car = Car(0, 0, 0, 0)
        car.load_car()
        CARS.append(car)

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.dy = -7
                elif event.key == pygame.K_s:
                    player.dy = 7
                if event.key == pygame.K_a:
                    player.dx = -7
                elif event.key == pygame.K_d:
                    player.dx = 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.dy = 0
                elif event.key == pygame.K_s:
                    player.dy = 0
                if event.key == pygame.K_a:
                    player.dx = 0
                elif event.key == pygame.K_d:
                    player.dx = 0


        SCREEN.fill(GRAY)

        '''GAME code'''

        player.draw_car()
        player.move_x()
        player.move_y()
        player.check_screen()

        for i in range(CAR_COUNT):
            CARS[i].draw_car()
            CARS[i].rect.y += CARS[i].dy
            if CARS[i].rect.y > WINDOW_HEIGHT:
                CARS[i].load_car()

        for i in range(CAR_COUNT):
            if player.check_collision(CARS[i], 5):

                if player.rect.x > CARS[i].rect.x:
                    CARS[i].rect.x -= 7
                else:
                    CARS[i].rect.x += 7

                if player.rect.y > CARS[i].rect.y:
                    CARS[i].rect.y -= CARS[i].dy
                else:
                    CARS[i].rect.y += CARS[i].dy



        for i in range(CAR_COUNT):
            for j in range(i +1, CAR_COUNT):
                if CARS[i].check_collision(CARS[j]):

                    if CARS[i].rect.x > CARS[j].rect.x:
                        CARS[i].rect.x += 4
                        CARS[j].rect.x -= 4
                    else:
                        CARS[i].rect.x -= 4
                        CARS[j].rect.x += 4

                    if CARS[i].rect.y > CARS[j].rect.y:
                        CARS[i].rect.y += CARS[i].dy
                        CARS[j].rect.y -= CARS[j].dy
                    else:
                        CARS[i].rect.y -= CARS[i].dy
                        CARS[j].rect.y += CARS[j].dy


        '''GAME code end'''





























        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()






















































































































































































































































































































































