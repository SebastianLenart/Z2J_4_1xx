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
        self.list_of_rabbits = []
        self.list_of_rabbits.append(Rabbit(self))
        self.display = Display(self)
        self.play_button = Button(self, "Gra")
        self.game_over_button = Button(self, "GAVE OVER")
        self.game_active = False
        self.game_over = False

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
                self._check_play_button(mouse_pos)
                if self.list_of_rabbits[-1].check_pos_any_rabbit(mouse_pos):
                    self.list_of_rabbits.pop()
                    self.list_of_rabbits.append(Rabbit(self))
                    self.start_ticks = pygame.time.get_ticks()
                    self.update_level()

    def update_level(self):
        self.settings.amount_rabbits -= 1
        if self.settings.amount_rabbits <= 0:
            self.settings.amount_rabbits = 5
            self.settings.increment_level()

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.game_active = True
            self.start_ticks = pygame.time.get_ticks()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.list_of_rabbits[-1].blitme()
        self.display.show_score()
        if not self.game_active and not self.game_over:
            self.play_button.draw_button()
        if self.game_over:
            self.game_over_button.draw_button()
        pygame.display.flip()  # odswiezanie okna

    def update_time(self):
        miliseconds = int((pygame.time.get_ticks() - self.start_ticks) / 1000)  # calculate how many seconds
        if self.before_time != miliseconds:
            self.seconds = miliseconds
            print(self.seconds)
            self.before_time = miliseconds
            self.check_deadtime()

    def check_deadtime(self):
        if self.seconds > self.settings.time:
            self.list_of_rabbits.pop()
            self.list_of_rabbits.append(Rabbit(self))
            self.start_ticks = pygame.time.get_ticks()
            if self.settings.decrement_life():
                self.game_active = False
                self.game_over = True


if __name__ == "__main__":
    game = Game()
    game.run()
