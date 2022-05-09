import pygame
import os
import cv2


class magnifier():
    def __init__(self, x, y, img):
        self.centerx = x;
        self.centery = y;
        self.screen = [
                [], [], [],
                [], [], [],
                [], [], []
                ];
        self.coordinates = [];
        self.coordlog = [];
        self.update(x, y, img)
    def mapper(self, img):
        x0 = self.centerx - 4;
        y0 = self.centery - 4;
        arrx = []
        for y in range(0, 9):
            for x in range(0, 9):
                if (x + x0) >= img.shape[1] or (y + y0) >= img.shape[0] or (x + x0) < 0 or (y + y0) < 0:
                    arrx.append(-1);
                else:
                    if img[y + y0][x + x0][3] == 255:
                        arrx.append(1);
                    else: 
                        arrx.append(0);

            self.screen[y] = arrx;
            arrx = [];

    def coordarray(self):
        arrx = []
        arry = []
        self.coordinates = [];
        for i in range(0, 9):
            arrx.append(self.centerx - 4 + i);
            arry.append(self.centery - 4 + i);
        self.coordinates.append(arrx);
        self.coordinates.append(arry);

    def update(self, x, y, img):
        self.centerx = x;
        self.centery = y;
        self.mapper(img);
        self.coordarray();
        self.coordlog.append(logger(self.centerx + 1, self.centery + 1).__dict__);



class logger():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;


class coordinatesys():
    def __init__(self):
        self.quadrant = [];
        self.white = (255, 255, 255);
        self.black = (0, 0, 0);
        self.red = (255, 0, 0);
        self.darko = (139, 64, 0);
        self.lighto = (255, 213, 128);
        arrx = []
        for y in range(0, 9):
            for x in range(0, 9):
                arrx.append(pygame.Surface((100, 100)));
            self.quadrant.append(arrx);
    def update(self, buff, screen):
        for y in range(0, 9):
            for x in range(0, 9):
                if buff[y][x] == 1:
                   self.quadrant[y][x].fill(self.black);
                elif buff[y][x] == 0:
                    self.quadrant[y][x].fill(self.white);
                else:
                    self.quadrant[y][x].fill(self.red);
                screen.blit(self.quadrant[y][x], (100 * (x + 1), 100 * (y + 1)))
        if buff[4][4] == 1: self.quadrant[4][4].fill(self.darko);
        else: self.quadrant[4][4].fill(self.lighto);
        screen.blit(self.quadrant[4][4], (100 * (5), 100 * (5)))



class axes():
    def __init__(self):
        self.axes = []
        arrx = []
        arry = []
        for i in range(0, 9):
            arrx.append(pygame.Surface((100, 100)))
            arry.append(pygame.Surface((100, 100)))
        self.axes.append(arrx);
        self.axes.append(arry);
        self.font = pygame.font.SysFont("Times new Roman", 18);
    def update(self, buff, screen):
        for i in range(0, 9):
            self.axes[0][i].fill((255, 255, 255));
            self.axes[1][i].fill((255, 255, 255));
            X = self.font.render(str(buff[0][i] + 1), 1, (0, 0, 0))
            Y = self.font.render(str(buff[1][i] + 1), 1, (0, 0, 0))

            self.axes[0][i].blit(X, (30, 30));
            self.axes[1][i].blit(Y, (30, 30));
            screen.blit(self.axes[0][i], ((i + 1) * 100, 0));
            screen.blit(self.axes[1][i], (0, (i + 1) * 100));



pygame.init()

WIDTH = 1000
HEIGHT = 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

img = cv2.imread("theultimate.png", cv2.IMREAD_UNCHANGED)
mag = magnifier(128, 139, img)
sys = coordinatesys();
ax = axes();
sys.update(mag.screen, SCREEN);
ax.update(mag.coordinates, SCREEN);
pygame.display.flip();

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                mag.update(mag.centerx - 1, mag.centery + 1, img);
                sys.update(mag.screen, SCREEN);
                ax.update(mag.coordinates, SCREEN);
            elif event.key == pygame.K_KP2:
                mag.update(mag.centerx, mag.centery + 1, img);
                sys.update(mag.screen, SCREEN);
                ax.update(mag.coordinates, SCREEN);
            elif event.key == pygame.K_KP3:
                mag.update(mag.centerx + 1, mag.centery + 1, img);
                sys.update(mag.screen, SCREEN);
                ax.update(mag.coordinates, SCREEN);
            elif event.key == pygame.K_KP4:
                mag.update(mag.centerx - 1, mag.centery, img);
                sys.update(mag.screen, SCREEN);
                ax.update(mag.coordinates, SCREEN);
            elif event.key == pygame.K_SPACE:
                print("cleared buffer")
                mag.coordlog = [];
            elif event.key == pygame.K_KP6:
                mag.update(mag.centerx + 1, mag.centery, img);
                sys.update(mag.screen, SCREEN);
                ax.update(mag.coordinates, SCREEN);
            elif event.key == pygame.K_KP7:
                mag.update(mag.centerx - 1, mag.centery - 1, img);
                sys.update(mag.screen, SCREEN);
                ax.update(mag.coordinates, SCREEN);
            elif event.key == pygame.K_KP8:
                mag.update(mag.centerx, mag.centery - 1, img);
                sys.update(mag.screen, SCREEN);
                ax.update(mag.coordinates, SCREEN);
            elif event.key == pygame.K_KP9:
                mag.update(mag.centerx + 1, mag.centery - 1, img);
                sys.update(mag.screen, SCREEN);
                ax.update(mag.coordinates, SCREEN);
            elif event.key == pygame.K_d:
                mag.coordlog.pop();
            elif event.key == pygame.K_c:
                os.system("clear");
            else: 
                print("", end = "\n\n"); 
                print(mag.coordlog);
            pygame.display.flip();

pygame.quit()
