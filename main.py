from constants import * 
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}"))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(screen)
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()
        
        pass

if __name__ == "__main__":
    main()
