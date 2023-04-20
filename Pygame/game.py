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
        self.before_time = 0
        print("time:", self.start_ticks)
        self.list_of_rabbits = []
        self.list_of_rabbits.append(Rabbit(self))
        self.display = Display(self)

    def run(self):
        while True:
            self._check_events()
            self.update_time()  # moze bedzie dzialac bez tego, w sensie ze w tle
            self.update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Zamkniecie okna")
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                if self.list_of_rabbits[-1].check_pos_any_rabbit(mouse_pos):
                    self.list_of_rabbits.pop()
                    self.list_of_rabbits.append(Rabbit(self))

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.list_of_rabbits[-1].blitme()
        pygame.display.flip()  # odswiezanie okna

    def update_time(self):
        seconds = int((pygame.time.get_ticks() - self.start_ticks) / 1000)  # calculate how many seconds
        if self.before_time != seconds:
            print(seconds)
            self.before_time = seconds

        return seconds


if __name__ == "__main__":
    # utworzenie egzemplarza gry i jej uruchomienie
    game = Game()
    game.run()
