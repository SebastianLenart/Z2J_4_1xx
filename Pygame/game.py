import pygame
from settings import Settings
from display import Display
from rabbit import Rabbit


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Game: rabbits")
        self.start_ticks = pygame.time.get_ticks()  # starter tick

        self.rabbit = Rabbit(self)

        display = Display(self)

    def run(self):
        while True:
            self._check_events()
            # self.update_time()
            self.update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Zamkniecie okna")
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                self.check_pos_any_rabbit(mouse_pos)

    def check_pos_any_rabbit(self, pos):
        pass

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rabbit.blitme()
        pygame.display.flip()  # odswiezanie okna


    def update_time(self):
        seconds = int((pygame.time.get_ticks() - self.start_ticks) / 1000)  # calculate how many seconds
        print(seconds)  # print how many seconds
        return seconds


if __name__ == "__main__":
    # utworzenie egzemplarza gry i jej uruchomienie
    game = Game()
    game.run()
