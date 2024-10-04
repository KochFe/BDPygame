import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gametime = pygame.time.Clock()
    # Calculate x and y to spawn the player in the middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # Create a Player instance
    player = Player(x, y)
    dt = 0 #
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()

        #end of loop
        #limit to 60 fps
        #save the elapsed time in seconds
        dt = gametime.tick(60) / 1000





if __name__ == "__main__":
    main()
