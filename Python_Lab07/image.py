import pygame

class Pic():
    def __init__(self, screen, name, width, height):
        self.screen = screen
        self.image_original = pygame.image.load(name)
        self.image_original = pygame.transform.scale(self.image_original, (width, height))
        self.image = self.image_original
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.angle = 0

    def output(self):
        self.screen.blit(self.image, self.rect)

    def rotate(self, angle):
        self.angle = angle
        self.image = pygame.transform.rotate(self.image_original, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
