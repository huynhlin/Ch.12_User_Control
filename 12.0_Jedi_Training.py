'''
Sign your name:________________
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!

'''
import arcade

SW = 640
SH = 480


class Box:
    def __init__(self, pos_x, pos_y, dx, dy, length, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.length = length
        self.color = color
        self.sound = arcade.load_sound("explosion.wav")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.length, self.length, self.color)

    def update_box(self):
        #edge control

        if self.pos_x + (self.length / 2) >= SW:
            self.pos_x = SW - (self.length / 2) - 1
            arcade.play_sound(self.sound)
        if self.pos_x < (self.length / 2):
            self.pos_x = (self.length / 2) + 1
            arcade.play_sound(self.sound)

        if self.pos_y + (self.length / 2) >= SH:
            self.pos_y = SH - (self.length / 2) - 1
            arcade.play_sound(self.sound)

        if self.pos_y < (self.length / 2):
            self.pos_y = (self.length / 2) + 1
            arcade.play_sound(self.sound)


        self.pos_x += self.dx
        self.pos_y += self.dy


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.l = 30
        self.rspeed = 0
        self.bspeed = 0
        self.rx = SW - self.l
        self.ry = SH - self.l
        self.bx = self.l
        self.by = self.l
        r = arcade.color.RED
        b = arcade.color.BLUE
        self.rbox = Box(self.rx, self.ry, self.rspeed, self.rspeed, self.l, r)
        self.bbox = Box(self.bx, self.by, self.bspeed, self.bspeed, self.l, b)
        self.boxes = []
        self.boxes.append(self.rbox)
        self.boxes.append(self.bbox)

    def on_draw(self):
        arcade.start_render()
        self.rbox.draw_box()
        self.bbox.draw_box()

    def on_update(self, dt):
        for box in self.boxes:
            box.update_box()

    def on_key_press(self, key, modifiers):
        # movement
        if key == arcade.key.LEFT:
            self.rbox.dx = -3
        elif key == arcade.key.RIGHT:
            self.rbox.dx = 3
        elif key == arcade.key.UP:
            self.rbox.dy = 3
        elif key == arcade.key.DOWN:
            self.rbox.dy = -3
        if key == arcade.key.A:
            self.bbox.dx = -4
        elif key == arcade.key.D:
            self.bbox.dx = 4
        elif key == arcade.key.W:
            self.bbox.dy = 4
        elif key == arcade.key.S:
            self.bbox.dy = -4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.rbox.dx = 0
        if key == arcade.key.RIGHT:
            self.rbox.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.rbox.dy = 0
        if key == arcade.key.A:
            self.bbox.dx = 0
        if key == arcade.key.D:
            self.bbox.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.bbox.dy = 0


def main():
    MyGame(SW, SH, "Test")
    arcade.run()


if __name__ == "__main__":
    main()
