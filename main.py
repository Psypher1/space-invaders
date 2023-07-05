import pygame, sys
from random import choice, randint

# Game imports
from game_code.player import Player
from game_code.obstacle import shape, Block
from game_code.alien import Alien, Extra
from game_code.laser import Laser


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

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)
        self.alien_direction = 1
        # Extra Alien setup
        self.extra_alien = pygame.sprite.GroupSingle()
        self.extra_alien_spawn_time = randint(400, 800)

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

    def alien_setup(
        self, rows, cols, x_distance=60, y_distance=48, x_offset=100, y_offset=80
    ):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                if row_index == 0:
                    alien_sprite = Alien("yellow", x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien("green", x, y)
                else:
                    alien_sprite = Alien("red", x, y)
                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens:
            all_aliens = self.aliens.sprites()
            for alien in all_aliens:
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, screen_height)
            self.alien_lasers.add(laser_sprite)

    def extra_alien_timer(self):
        self.extra_alien_spawn_time -= 1
        if self.extra_alien_spawn_time <= 0:
            self.extra_alien.add(Extra(choice(["right", "left"]), screen_width))
            self.extra_alien_spawn_time = randint(400, 800)

    def collision_checks(self):
        # player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

    def run(self):
        self.player.update()
        self.aliens.update(self.alien_direction)
        self.alien_position_checker()
        # self.alien_shoot()  # running it here would cause a flood of lasers
        self.alien_lasers.update()
        self.extra_alien_timer()
        self.extra_alien.update()
        self.collision_checks()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra_alien.draw(screen)
        # update all sprite groups
        # draw all sprite groups


if __name__ == "__main__":
    pygame.init()
    screen_width = 700
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    ALLIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALLIENLASER, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALLIENLASER:
                game.alien_shoot()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
