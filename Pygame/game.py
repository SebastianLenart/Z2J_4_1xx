import pygame
from settings import Settings


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))
        pygame.display.set_caption("Game: rabbits")





    def run(self):
        pass






if __name__ == "__main__":
    # utworzenie egzemplarza gry i jej uruchomienie
    game = Game()
    game.run()
