from constants import * 
from player import *
from asteroid import * 
from asteroidfield import *
from shot import * 
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
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updateable, drawable)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while running: 
        print(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        #player.update(dt)
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                print("Game Over!")
                return
        for sprite in drawable:
            sprite.draw(screen)
        #player.draw(screen)
        
        pygame.display.flip()
        
        pass
        dt = Clock.tick(FPS) / 1000
if __name__ == "__main__":
    main()
