import pygame, sys
from player import Player

class Game:
    def __init__(self) -> None:
        player_sprite = Player((screen_width/2, screen_height - 20))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.draw(screen)
        # update all sprite groups
        # draw all sprite groups
        


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
                pygame.quit()
                sys.exit()
        screen.fill((30,30, 30))
        game.run( )

        pygame.display.flip()
        clock.tick(60)