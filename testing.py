import arcade
import random

SW = 640
SH = 480
speed = 3
bullet_speed = 6

#INSTRUCTIONS
#WASD/ARROW KEYS TO MOVE
#L/R SHIFT TO SHOOT


class Guy(arcade.Sprite):
    def __init__(self, colorvar, color):
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
        self.shoot_sound = arcade.load_sound("laser.wav")
        self.time_since_fire = 1.0
        self.able_to_shoot = True
        # self.death_sound = arcade.load_sound("sounds/mp3s/death.mp3")
        # self.victory_sound = arcade.load_sound("sounds/mp3s/victory.mp3")
        self.dx = 0
        self.dy = 0
        self.shooting = False
        self.l = False
        self.col = color

    def update_guy(self):

        if self.center_x < -35:
            self.center_x = SW + 35
        if self.center_x > SW + 35:
            self.center_x = -35

        if self.center_y < -50:
            self.center_y = SH + 50
        if self.center_y > SH + 50:
            self.center_y = -50

        self.center_x += self.dx
        self.center_y += self.dy

        if self.shooting:
            if self.l:
                self.texture = self.textures[3]
            else:
                self.texture = self.textures[1]
        if not self.shooting:
            if not self.l:
                self.texture = self.textures[0]
            else:
                self.texture = self.textures[2]


class Bullet():
    def __init__(self, iden, x, y, dx, size, l):
        self.iden = iden
        self.pos_x = x
        self.pos_y = y
        self.dx = dx
        self.size = size
        self.l = l

    def draw(self, iden):
        if iden == 0:
            arcade.draw_rectangle_filled(self.pos_x+5, self.pos_y+10, self.size, self.size, arcade.color_from_hex_string("ed1c23"))
        else:
            arcade.draw_rectangle_filled(self.pos_x+5, self.pos_y+10, self.size, self.size, arcade.color_from_hex_string("4d6ef3"))

    # class Bullet(arcade.Sprite):
#     def __init__(self, x, y, size, speed, dmg, iden, l):
#         super().__init__()
#         self.pos_x = x
#         self.pos_y = y
#         self.size = size
#         self.speed = speed
#         self.dmg = dmg
#         self.textures = []
#         self.red = arcade.load_texture(f"rbullet.png")
#         self.textures.append(self.red)
#         self.blue = arcade.load_texture(f"bbullet.png")
#         self.textures.append(self.blue)
#         self.texture = self.textures[iden]
#         self.l = l
#
#     def make_bullet(self, iden):
#         if iden == 0:
#             sprite = arcade.Sprite(f"rbullet.png", 1, self.pos_x, self.pos_y)
#         else:
#             sprite = arcade.Sprite(f"bbullet.png", 1, self.pos_x, self.pos_y)
#         return sprite


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color_from_hex_string("ffdcdc"))
        self.redguy = Guy("r", "ed1c23")
        self.blueguy = Guy("b", "709ad1")
        self.redguy.center_x = random.randint(1+40, SW-40)
        self.redguy.center_y = random.randint(1+40, SH-40)
        self.blueguy.center_x = random.randint(1+40, SW-40)
        self.blueguy.center_y = random.randint(1+40, SH-40)
        self.bbullet_list = []
        self.rbullet_list = []

    def on_draw(self):
        arcade.start_render()
        self.redguy.draw()
        self.blueguy.draw()
        for i in self.bbullet_list:
            i.draw(1)
        for i in self.rbullet_list:
            i.draw(0)

    def on_update(self, dt):
        self.redguy.update_guy()
        self.redguy.time_since_fire += dt
        self.blueguy.time_since_fire += dt
        self.blueguy.update_guy()
        for bullet in self.bbullet_list:
            if bullet.l:
                bullet.pos_x -= bullet_speed
            else:
                bullet.pos_x += bullet_speed

            if bullet.pos_x > SW + 50 or bullet.pos_x < -50 or bullet.pos_y > SH + 50 or bullet.pos_y < -50:
                ""
                # bullet.kill()


        for bullet in self.rbullet_list:
            if bullet.l:
                bullet.pos_x -= bullet_speed
            else:
                bullet.pos_x += bullet_speed

            if bullet.pos_x > SW + 50 or bullet.pos_x < -50 or bullet.pos_y > SH + 50 or bullet.pos_y < -50:
                ""
                # bullet.kill()

    def on_key_press(self, key, modifiers):
        #movement
        if key == arcade.key.LEFT:
            self.redguy.dx = -speed
            self.redguy.l = True
        elif key == arcade.key.RIGHT:
            self.redguy.dx = speed
            self.redguy.l = False
        elif key == arcade.key.UP:
            self.redguy.dy = speed
        elif key == arcade.key.DOWN:
            self.redguy.dy = -speed
        if key == arcade.key.A:
            self.blueguy.dx = -speed
            self.blueguy.l = True
        elif key == arcade.key.D:
            self.blueguy.dx = speed
            self.blueguy.l = False
        elif key == arcade.key.W:
            self.blueguy.dy = speed
        elif key == arcade.key.S:
            self.blueguy.dy = -speed

        #shooting
        if key == arcade.key.LSHIFT:
            if self.blueguy.time_since_fire >= 0.6:
                self.blueguy.able_to_shoot = True
            else:
                self.blueguy.able_to_shoot = False
            if not self.blueguy.shooting and self.blueguy.able_to_shoot:
                self.blueguy.shooting = True
                arcade.play_sound(self.redguy.shoot_sound, 0.5)
                bullet = Bullet(0, self.blueguy.center_x, self.blueguy.center_y, bullet_speed, 10, self.blueguy.l)
                self.bbullet_list.append(bullet)
                self.blueguy.time_since_fire = 0

        if key == arcade.key.RSHIFT:
            if self.redguy.time_since_fire >= 0.6:
                self.redguy.able_to_shoot = True
            else:
                self.redguy.able_to_shoot = False
            if not self.redguy.shooting and self.redguy.able_to_shoot:
                self.redguy.shooting = True
                arcade.play_sound(self.redguy.shoot_sound, 0.5)
                bullet = Bullet(1, self.redguy.center_x, self.redguy.center_y, bullet_speed, 10, self.redguy.l)
                self.rbullet_list.append(bullet)
                self.redguy.time_since_fire = 0

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.redguy.dx = 0
            self.redguy.l = True

        if key == arcade.key.RIGHT:
            self.redguy.dx = 0
            self.redguy.l = False

        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.redguy.dy = 0

        if key == arcade.key.A:
            self.blueguy.l = True
            self.blueguy.dx = 0

        if key == arcade.key.D:
            self.blueguy.dx = 0
            self.blueguy.l = False

        elif key == arcade.key.W or key == arcade.key.S:
            self.blueguy.dy = 0

        if key == arcade.key.LSHIFT:
            if self.blueguy.shooting:
                self.blueguy.shooting = False

        if key == arcade.key.RSHIFT:
            if self.redguy.shooting:
                self.redguy.shooting = False


def main():
    MyGame(SW, SH, "TRIPLE A FPS GAME")
    arcade.run()


if __name__ == "__main__":
    main()