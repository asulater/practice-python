import pygame

pygame.init() # Initialization

screen_width = 480 
screen_height = 640 
screent = pygame.display.set_mode((screen_width, screen_height))

# set display title 
pygame.display.set_caption("Game") # Game title

# Event Loop
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close windows
            running = False

