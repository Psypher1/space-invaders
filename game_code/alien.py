from typing import Any
import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y) -> None:
        super().__init__()
        file_path = "./assets/graphics/" + color + ".png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        if color == "yelow":
            self.value = 300
        if color == "green":
            self.value = 200
        elif color == "red":
            self.value = 100

    def update(self, direction) -> None:
        self.rect.x += direction


class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width) -> None:
        super().__init__()
        self.image = pygame.image.load("./assets/graphics/extra.png").convert_alpha()

        if side == "right":
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft=(x, 80))

    def update(self):
        self.rect.x += self.speed
