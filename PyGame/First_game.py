import pygame

screen_size = [360, 600]

screen = pygame.display.set_mode(screen_size)

background = pygame.image.load("profile-pic1.png")

screen.blit(background, [0, 0])

keep_alive = True
i = 0
while keep_alive:
    screen.blit(background, [i, 0])
    pygame.display.update()
    i += 1