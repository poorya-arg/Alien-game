import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start new aliens near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store its exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """"draw"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """if alien is at the edge return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move to right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

