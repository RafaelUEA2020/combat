import pygame
import os

pygame.init()

screen_options = [pygame.RESIZABLE, pygame.FULLSCREEN]

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

menu_screen = pygame.display.set_mode((screen_width - 100, screen_height - 100), screen_options[0])
pygame.display.set_caption('Tankpygame ta ligado!')

def start_game():
    running = True
    while running:
        menu_screen.fill((0, 0, 0))
        pygame.display.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
