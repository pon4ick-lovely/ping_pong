import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong game"

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.1)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class ComputerBar(Bar):
    def __init__(self, ball):
        super().__init__()
        self.ball = ball

    def update(self):
        if self.center_y < self.ball.center_y:
            self.change_x = 3
        elif self.center_y > self.ball.center_y:
            self.change_x = -3
        else:
            self.change_x = 0
        super().update()

class Ball(arcade.Sprite):
    def __init__(self) -> object:
        super().__init__('ball.png', 0.05)
        self.change_x = 3
        self.change_y = 3

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y

class Game(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title)
        self.bar = Bar()
        self.ball = Ball()
        self.computer_bar = ComputerBar(self.ball)
        self.setup()
        self.player_score = 0
        self.computer_score = 0

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.computer_bar.center_x = SCREEN_WIDTH / 2
        self.computer_bar.center_y = 4 * SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.computer_bar.draw()
        self.ball.draw()
        arcade.draw_text(f"Player: {self.player_score}", 10, SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Computer: {self.computer_score}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
            self.player_score += 1
        if arcade.check_for_collision(self.computer_bar, self.ball):
            self.ball.change_y = -self.ball.change_y
            self.computer_score += 1
        self.ball.update()
        self.bar.update()
        self.computer_bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()