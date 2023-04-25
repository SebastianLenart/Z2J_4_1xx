import pygame.font


class Display:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.level_image = None
        self.life_image = None
        self.time_image = None
        self.rabbits_image = None
        self.color = (0, 255, 0)

        # czcionka
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)  # obiekt czcionki

        self.prep_level()
        self.prep_life()
        self.prep_time()
        self.prep_rabbits()

    def prep_level(self):
        level_str = "Level: ".join(str(self.settings.level))
        self.level_image = self.font.render(str("Level: ") + level_str, True,
                                            self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 20

    def prep_life(self):
        life_str = (str(self.settings.life))
        self.life_image = self.font.render(str("Life: ") + life_str, True,
                                           self.text_color)
        self.life_rect = self.life_image.get_rect()
        self.life_rect.right = self.screen_rect.right - 350
        self.life_rect.top = 20

    def prep_time(self):
        time_str = str(self.game.seconds)
        self.time_image = self.font.render(str("Time: ") + time_str, True,
                                           self.text_color)
        self.time_rect = self.time_image.get_rect()
        self.time_rect.right = self.screen_rect.left + self.time_rect.width
        self.time_rect.top = 20

    def prep_rabbits(self):
        rabbits_str = (str(self.settings.amount_rabbits))
        self.rabbits_image = self.font.render(str("Rabbits: ") + rabbits_str, True,
                                           self.text_color)
        self.rabbits_rect = self.rabbits_image.get_rect()
        self.rabbits_rect.right = self.screen_rect.right - 320
        self.rabbits_rect.top = 60

    def show_score(self):
        self.prep_level()
        self.prep_life()
        self.prep_time()
        self.prep_rabbits()

        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.life_image, self.life_rect)
        self.screen.blit(self.time_image, self.time_rect)
        self.screen.blit(self.rabbits_image, self.rabbits_rect)
