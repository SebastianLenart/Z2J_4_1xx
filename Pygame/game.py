import pygame
from settings import Settings
from display import Display
from rabbit import Rabbit
from button import Button

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Game: rabbits")
        self.start_ticks = pygame.time.get_ticks()
        self.before_time = 0
        self.seconds = 0
        print("time:", self.start_ticks)
        self.list_of_rabbits = []
        self.list_of_rabbits.append(Rabbit(self))
        self.display = Display(self)
        self.play_button = Button(self, "Gra")
        self.game_active = False

    def run(self):
        while True:
            self._check_events()
            if self.game_active:
                self.update_time()
            self.update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Zamkniecie okna")
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.list_of_rabbits[-1].check_pos_any_rabbit(mouse_pos):
                    self.list_of_rabbits.pop()
                    self.list_of_rabbits.append(Rabbit(self))
                    self.start_ticks = pygame.time.get_ticks()

    def update_screen(self):
        if not self.game_active:
            self.play_button.draw_button()
            self.game_active = True
            return
        self.screen.fill(self.settings.bg_color)
        self.list_of_rabbits[-1].blitme()
        pygame.display.flip()  # odswiezanie okna

    def update_time(self):
        miliseconds = int((pygame.time.get_ticks() - self.start_ticks) / 1000)  # calculate how many seconds
        if self.before_time != miliseconds:
            self.seconds = miliseconds
            print(self.seconds)
            self.before_time = miliseconds


if __name__ == "__main__":
    game = Game()
    game.run()
