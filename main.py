import random
import pygame , sys
from pygame.locals import *

pygame.init()

# dimentions
WIDTH = 500
HEIGHT = 500

# colors
WHITE = (255,255,255)
SKY = (153,217,234)
LAND = (117,47,0)

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Wave Function Colapsing Algorithm")

class VerticleLine:
    def __init__(self, width, height):
        self.img = pygame.image.load("verticleLine.png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.imgRect = self.img.get_rect()

    def draw(self, x, y):
        self.imgRect.left = x
        self.imgRect.top = y
        win.blit(self.img, self.imgRect)

    def next(self,top=False,down=False):
        # first element can be 0 , 1 or -1 which represents that the next block can be at same level , upper heigth or lower height respectively
        # the second element will be the type of block
        possible = ("verticleLine", "sideToUp", "sideToDown")
        return [0, possible[random.randint(0,2)]]

class SideToUp:
    def __init__(self, width, height):
        self.img = pygame.image.load("sideToUp.png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.imgRect = self.img.get_rect()

    def draw(self, x, y):
        self.imgRect.left = x
        self.imgRect.top = y
        win.blit(self.img, self.imgRect)

    def next(self, top=False,down=False):
        # first element can be 0 , 1 or -1 which represents that the next block can be at same level , upper heigth or lower height respectively
        # the second element will be the type of block
        possible = ("diagonalUp", "downToSide", "upToSide")
        if top:
            return [0, possible[2]]
        return [1, possible[random.randint(0,1)]]

class SideToDown:
    def __init__(self, width, height):
        self.img = pygame.image.load("sideToDown.png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.imgRect = self.img.get_rect()

    def draw(self, x, y):
        self.imgRect.left = x
        self.imgRect.top = y
        win.blit(self.img, self.imgRect)

    def next(self, top=False, down=False):
        # first element can be 0 , 1 or -1 which represents that the next block can be at same level , upper heigth or lower height respectively
        # the second element will be the type of block
        possible = ("diagonal", "upToSide", "downToSide")
        if down:
            return [0, possible[2]]
        return [-1, possible[random.randint(0,1)]]

class Diagonal:
    def __init__(self, width, height):
        self.img = pygame.image.load("diagonal.png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.imgRect = self.img.get_rect()

    def draw(self, x, y):
        self.imgRect.left = x
        self.imgRect.top = y
        win.blit(self.img, self.imgRect)

    def next(self, top=False, down=False):
        # first element can be 0 , 1 or -1 which represents that the next block can be at same level , upper heigth or lower height respectively
        # the second element will be the type of block
        possible = ("diagonal", "upToSide", "diagonalUp")
        if down:
            return [0, possible[2]]
        return [-1, possible[random.randint(0,1)]]

class DiagonalUp:
    def __init__(self, width, height):
        self.img = pygame.image.load("diagonalUp.png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.imgRect = self.img.get_rect()

    def draw(self, x, y):
        self.imgRect.left = x
        self.imgRect.top = y
        win.blit(self.img, self.imgRect)

    def next(self, top=False,down=False):
        # first element can be 0 , 1 or -1 which represents that the next block can be at same level , upper heigth or lower height respectively
        # the second element will be the type of block
        possible = ("diagonalUp", "downToSide", "diagonal")
        if top:
            return [0, possible[2]]
        return [1, possible[random.randint(0,1)]]

class DownToSide:
    def __init__(self, width, height):
        self.img = pygame.image.load("downToSide.png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.imgRect = self.img.get_rect()

    def draw(self, x, y):
        self.imgRect.left = x
        self.imgRect.top = y
        win.blit(self.img, self.imgRect)

    def next(self,top=False,down=False):
        # first element can be 0 , 1 or -1 which represents that the next block can be at same level , upper heigth or lower height respectively
        # the second element will be the type of block
        possible = ("verticleLine", "sideToUp", "sideToDown")
        return [0, possible[random.randint(0,2)]]

class UpToSide:
    def __init__(self, width, height):
        self.img = pygame.image.load("upToSide.png")
        self.img = pygame.transform.scale(self.img, (width, height))
        self.imgRect = self.img.get_rect()

    def draw(self, x, y):
        self.imgRect.left = x
        self.imgRect.top = y
        win.blit(self.img, self.imgRect)

    def next(self,top=False,down=False):
        # first element can be 0 , 1 or -1 which represents that the next block can be at same level , upper heigth or lower height respectively
        # the second element will be the type of block
        possible = ("verticleLine", "sideToUp", "sideToDown")
        return [0, possible[random.randint(0,2)]]

def draw():
    global numberOfBoxes, smallBoxHeight, smallBoxWidth, verticleLine, diagonal, diagonalUp, sideToUp, sideToDown, upToSide, downToSide
    
    x = 0
    y = 0
    for i in range(numberOfBoxes):
        if i == 0:
            y = random.randint(0,numberOfBoxes-1)
            possible = [diagonal, diagonalUp, verticleLine, sideToUp, sideToDown, upToSide, downToSide]
            block = possible[random.randint(0,6)]
        else:
            if available[0] == 1:
                y -= 1
            elif available[0] == -1:
                y += 1
            if available[1] == "verticleLine":
                block = verticleLine
            elif available[1] == "diagonal":
                block = diagonal
            elif available[1] == "diagonalUp":
                block = diagonalUp
            elif available[1] == "sideToUp":
                block = sideToUp
            elif available[1] == "sideToDown":
                block = sideToDown
            elif available[1] == "upToSide":
                block = upToSide
            elif available[1] == "downToSide":
                block = downToSide
        block.draw(x,y*smallBoxHeight)
        pygame.draw.rect(win, SKY, (x,0,smallBoxWidth,smallBoxHeight*y))
        pygame.draw.rect(win, LAND, (x,(y+1)*smallBoxHeight,smallBoxWidth,((numberOfBoxes-1)-y)*smallBoxHeight))
        available = block.next(y==0,y==numberOfBoxes-1)
        #print(available)
        x += smallBoxWidth
        
def main():
    global numberOfBoxes, smallBoxHeight, smallBoxWidth, verticleLine, diagonal, diagonalUp, sideToUp, sideToDown, upToSide, downToSide
    numberOfBoxes = 50
    smallBoxHeight = HEIGHT/numberOfBoxes
    smallBoxWidth = WIDTH/numberOfBoxes
    verticleLine = VerticleLine(smallBoxWidth,smallBoxHeight)
    diagonal = Diagonal(smallBoxWidth,smallBoxHeight)
    diagonalUp = DiagonalUp(smallBoxWidth,smallBoxHeight)
    sideToUp = SideToUp(smallBoxWidth,smallBoxHeight)
    sideToDown = SideToDown(smallBoxWidth,smallBoxHeight)
    downToSide = DownToSide(smallBoxWidth,smallBoxHeight)
    upToSide = UpToSide(smallBoxWidth,smallBoxHeight)
    do = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            elif event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    do = True
        if do:
            draw()
            pygame.display.update()
            do = False

if __name__ == '__main__':
    main()
