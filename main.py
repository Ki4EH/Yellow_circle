import pygame
import random

if __name__ == '__main__':
    size = width, height = random.randint(100, 600), random.randint(100, 600)
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    # screen2.fill((0, 0, 255))
    screen.fill((0, 0, 255))
    x1, y1, w, h = 0, 0, 0, 0
    drawing = False  # режим рисования выключен
    running = True
    v = 200
    fps = 20
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = 20
                screen.fill((0, 0, 255))
                for i in range(20):
                    x += v / fps
                    clock.tick(fps)
                    print(x)
                    pygame.draw.circle(screen, (255, 255, 0), event.pos, x)
                    pygame.display.flip()
        pygame.display.flip()
