import pygame
import random

LENGTH = 640
WIDTH = 512

def getGrid(coords):
    x = coords[0] // 32
    y = coords[1] // 32
    return (x, y)

def drawGrid(screen):
    for i in range(0, WIDTH, 32):
        pygame.draw.line(screen, "black", (0, i), (LENGTH, i))
    for i in range(0, LENGTH, 32):
        pygame.draw.line(screen, "black", (i, 0), (i, WIDTH))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((LENGTH, WIDTH))
        clock = pygame.time.Clock()
        running = True
        mole_x = random.randrange(0, 19) * 32
        mole_y = random.randrange(0,15) * 32
        while running:
            screen.fill("light green")
            drawGrid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coords = event.pos
                    if getGrid((mole_x, mole_y)) == getGrid(coords):
                        mole_x = random.randrange(0, 19) * 32
                        mole_y = random.randrange(0,15) * 32

                    
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
