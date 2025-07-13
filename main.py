from constants import * 
from player import *
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}"))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(screen)
    running = True
    Clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while running: 
        print(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()
        
        pass
        dt = Clock.tick(FPS) / 1000
if __name__ == "__main__":
    main()
