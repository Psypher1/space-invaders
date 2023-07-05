import pygame
from pygame.sprite import _Group


class Obstacle(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
