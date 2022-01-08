import pygame

class Image:
    def __init__(self, image, x = 0, y = 0):
        self.image = pygame.image.load(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y