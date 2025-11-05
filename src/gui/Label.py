import pygame
from config import HEIGHT, WIDTH

class Label:
    def __init__(self, txt, location, screen):
        self.screen = screen

        self.size = 16
        self.font = pygame.font.SysFont("Segoe Print", self.size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, "#000000")
        self.txt_rect = self.txt_surf.get_rect()

        self.surface = pygame.surface.Surface((self.size, self.size))
        self.rect = self.surface.get_rect(topleft=location)

    def draw(self):
        self.screen.blit(self.surface, self.rect)

    def update(self):
        self.surface.fill("#FFFFFF")
        self.txt_surf = self.font.render(self.txt, True, "#000000")
        self.surface.blit(self.txt_surf, self.txt_rect)