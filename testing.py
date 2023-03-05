import arcade
import random

SW = 640
SH = 480
speed = 3


class Guy(arcade.Sprite):
    def __init__(self, colorvar):
        super().__init__()
        self.textures = []
        self.test = arcade.load_texture(f"{colorvar}.png")
        self.textures.append(self.test)
        self.shoot = arcade.load_texture(f"{colorvar}shoot.png")
        self.textures.append(self.shoot)
        self.fliptest = arcade.load_texture(f"{colorvar}.png", flipped_horizontally=True)
        self.textures.append(self.fliptest)
        self.flipshoot = arcade.load_texture(f"{colorvar}shoot.png", flipped_horizontally=True)
        self.textures.append(self.flipshoot)
        self.texture = self.textures[0]
        self.set_position(random.randint(1, SH), random.randint(1, SH))
        # self.center_x = SW/2
        # self.center_y = SH/2
        self.dx = 0
        self.dy = 0
        self.shooting = False
        self.left = False

    def update_guy(self):

        # if self.left:
        #     self.texture = self.textures[2]
        # else:
        #     self.texture = self.textures[0]
    #     if self.pos_x + self.rad >= SW or self.pos_x < self.rad:
    #         self.dx *= -1
    #
    #     if self.pos_y + self.rad >= SH or self.pos_y - self.rad <= 0:
    #         self.dy *= -1
    #
        # if self.center_x < 0:
        #     self.center_x = SW
        # if self.center_x > SW:
        #     self.center_x = 0
        #
        # if self.center_y < 0:
        #     self.center_y = SH
        # if self.center_y > SH:
        #     self.center_y = 0

        self.center_x += self.dx
        self.center_y += self.dy

        if self.shooting:
            if self.left:
                self.texture = self.textures[3]
            else:
                self.texture = self.textures[1]
        if not self.shooting:
            if self.left:
                self.texture = self.textures[2]
            else:
                self.texture = self.textures[0]


class Bullet:
    def __init__(self):
        ""


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color_from_hex_string("ffdcdc"))
        redvar = "r"
        bluevar = "b"
        self.redguy = Guy(redvar)
        self.blueguy = Guy(bluevar)

    def on_draw(self):
        arcade.start_render()
        self.redguy.draw()
        self.blueguy.draw()

    def on_update(self, dt):
        self.redguy.update_guy()
        self.blueguy.update_guy()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.redguy.dx = -speed
            self.redguy.left = True
            self.redguy.texture = self.redguy.textures[2]
        elif key == arcade.key.RIGHT:
            self.redguy.dx = speed
            self.redguy.left = False
            self.redguy.texture = self.redguy.textures[0]
        elif key == arcade.key.UP:
            self.redguy.dy = speed
        elif key == arcade.key.DOWN:
            self.redguy.dy = -speed
        if key == arcade.key.A:
            self.blueguy.dx = -speed
            self.blueguy.left = True
        elif key == arcade.key.D:
            self.blueguy.dx = speed
            self.blueguy.left = False
        elif key == arcade.key.W:
            self.blueguy.dy = speed
        elif key == arcade.key.S:
            self.blueguy.dy = -speed

        if key == arcade.key.LSHIFT:
            if not self.blueguy.shooting:
                self.blueguy.shooting = True
            else:
                self.blueguy.shooting = False

        if key == arcade.key.RSHIFT:
            if not self.redguy.shooting:
                self.redguy.shooting = True
            else:
                self.redguy.shooting = False

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.redguy.dx = 0
            self.redguy.left = True
            self.redguy.texture = self.redguy.textures[2]
        if key == arcade.key.RIGHT:
            self.redguy.dx = 0
            self.redguy.left = False
            self.redguy.texture = self.redguy.textures[0]

        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.redguy.dy = 0

        if key == arcade.key.A:
            self.blueguy.left = True
            self.blueguy.dx = 0
            self.blueguy.texture = self.blueguy.textures[2]

        if key == arcade.key.D:
            self.blueguy.dx = 0
            self.blueguy.left = False
            self.blueguy.texture = self.blueguy.textures[0]

        elif key == arcade.key.W or key == arcade.key.S:
            self.blueguy.dy = 0

        if key == arcade.key.LSHIFT:
            if not self.blueguy.shooting:
                self.blueguy.shooting = True
            else:
                self.blueguy.shooting = False

        if key == arcade.key.RSHIFT:
            if not self.redguy.shooting:
                self.redguy.shooting = True
            else:
                self.redguy.shooting = False

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.guy.pos_x = x
    #     self.guy.pos_y = y
    #
    # def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
    #     if button == arcade.MOUSE_BUTTON_LEFT:
    #         print("Left mouse button pressed at", x, y)
    #     elif button == arcade.MOUSE_BUTTON_RIGHT:
    #         print("RIght mouse button press at", x, y)


def main():
    MyGame(SW, SH, "User Control")
    arcade.run()


if __name__ == "__main__":
    main()
