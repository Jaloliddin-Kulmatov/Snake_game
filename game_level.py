from turtle import Screen
class Game_level:
    def __init__(self):
        screen = Screen()
        self.difficulty = screen.numinput("Snake game", "Choose difficulty (1 is the fastest):", 1, minval=1, maxval=10)


