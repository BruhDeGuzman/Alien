# A module that contains the ship items

import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the game image and get it's rect
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


