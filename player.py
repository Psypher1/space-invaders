import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image= pygame.image.load("./assets/graphics/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)