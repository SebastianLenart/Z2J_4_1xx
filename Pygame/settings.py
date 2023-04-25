class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.life = 1
        self.amount_rabbits = 5
        self.time = 5
        self.level = 1

    def decrement_life(self):
        self.life -= 1
        if self.life <= 0:
            print("GAME OVER")
            return True

    def decrement_time(self):
        self.time -= 1
        if self.time <= 1:
            print("WIN")
            exit()

    def increment_level(self):
        self.level += 1
