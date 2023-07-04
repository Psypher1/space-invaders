import pygame, sys

class Game:
    def __init__(self) -> None:
        pass

    def run(self):
        # update all sprite groups
        # draw all sprite groups
        pass


if __name__ == "__main__":
    pygame.init()
    screen_width = 700
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()
        screen.fill((30,30, 30))
        game.run( )

        pygame.display.flip()
        clock.tick(60)