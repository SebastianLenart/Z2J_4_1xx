import pygame.image
import random


class Rabbit:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        width = self.screen_rect.right
        height = self.screen_rect.height
        self.settings = game.settings

        self.image = pygame.image.load("C:\\Users\\Sebastian\\Z2J_4_1xx\\Pygame\\krolik.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(0, height - self.rect.height)

    def check_pos_any_rabbit(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
