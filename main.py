import pygame, sys
from game_code.player import Player
from game_code.obstacle import shape, Block


class Game:
    def __init__(self) -> None:
        # Player setup
        player_sprite = Player((screen_width / 2, screen_height - 10), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Obstacle setup
        self.shape = shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [
            num * (screen_width / self.obstacle_amount)
            for num in range(self.obstacle_amount)
        ]
        # self.create_obstacle(40, 500)
        self.create_multiple_obstacles(
            *self.obstacle_x_positions, x_start=screen_width / 12, y_start=500
        )  # use * because position come in as list - unpack them

    def create_obstacle(self, x_start, y_start, offset_x):
        # enumarate to know where we are in the shape
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = Block(self.block_size, (247, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def run(self):
        self.player.update()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)
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
        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
