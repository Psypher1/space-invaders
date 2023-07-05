import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y) -> None:
        super().__init__()
        file_path = "./assets/graphics/" + color + ".png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
