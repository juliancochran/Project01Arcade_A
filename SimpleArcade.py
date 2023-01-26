# This is a simple 2D game where the player has to avoid tokens bouncing
# around a screen
# Thursday 01/26/2023
__author__ = 'Julian Cochran'
# hello this is a test

"""
Project found at these URLs and modifed:
https://api.arcade.academy/en/latest/examples/sprite_move_keyboard.html#sprite-move-keyboard
https://api.arcade.academy/en/latest/examples/sprite_collect_coins_move_bouncing.html#sprite-collect-coins-move-bouncing

Better Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
This is slightly better than sprite_move_keyboard.py example
in how it works, but also slightly more complex.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard_better
"""

import arcade
import random

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "+* DODGE THE DUMMIES *+"

MOVEMENT_SPEED = 5
IMAGES = ['slimeBlue.png', 'slimeGreen.png', 'slimePurple.png']

class Slime(arcade.Sprite):

    bounces = 0
    img_index = 0

    def update(self):
        """ Move the slime """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 1:
            self.left = 2
            self.change_x *= -1
            self.bounces += 1
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH- 2
            self.change_x *= -1
            self.bounces += 1
        if self.bottom < 1:
            self.bottom = 2
            self.change_y *= -1
            self.bounces += 1
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT-2
            self.change_y *= -1
            self.bounces += 1

        if self.bounces == 20:
            #self.filename = ":resources:images/enemies/"+IMAGES[1]
            if self.change_x > 0:
                self.change_x += 1
            else:
                self.change_x -= 1

            if self.change_y > 0:
                self.change_y += 1
            else:
                self.change_y -= 1
            #print('DEBUG THIS SPRITE', self.bounces)
            self.bounces = 0

class Player(arcade.Sprite):

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        '''if self.left < 1:
            self.left = 1
        elif self.right > SCREEN_WIDTH - (128/2):
            self.right = SCREEN_WIDTH - 127
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 128:
            self.top = SCREEN_HEIGHT - 127'''


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None
        self.slime_list = None
        # Set up the player info
        self.player_sprite = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK_BEAN)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.slime_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                    SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(5):
            temp = Slime(":resources:images/enemies/"+IMAGES[0],
                                        SPRITE_SCALING)
            temp.center_x = SCREEN_WIDTH/2
            temp.center_y = SCREEN_HEIGHT/2
            temp.change_x = random.choice([-4, -3, -2, 2, 3, 4])
            temp.change_y = random.choice([-4, -3, -2, 2, 3, 4])
            self.slime_list.append(temp)


    def on_draw(self):
        """ Render the screen. """

        # Clear the screen
        self.clear()

        # Draw all the sprites.
        self.player_list.draw()
        self.slime_list.draw()


    def update_player_speed(self):

        # Calculate speed based on the keys pressed

        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def update_slime_speed(self):

        for ss in self.slime_list:
            ss.update()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player_list.update()
        self.slime_list.update()
        self.update_slime_speed()
        #if arcade.check_for_collision(self.player_sprite, self.slime_sprite):
            #self.player_sprite.remove_from_sprite_lists()


    def on_key_press(self, key, modifiers):

        """Called whenever a key is pressed. """



        if key == arcade.key.UP:

            self.up_pressed = True
            self.update_player_speed()

        elif key == arcade.key.DOWN:

            self.down_pressed = True
            self.update_player_speed()

        elif key == arcade.key.LEFT:

            self.left_pressed = True
            self.update_player_speed()

        elif key == arcade.key.RIGHT:

            self.right_pressed = True
            self.update_player_speed()



    def on_key_release(self, key, modifiers):

        """Called when the user releases a key. """



        if key == arcade.key.UP:

            self.up_pressed = False

            self.update_player_speed()

        elif key == arcade.key.DOWN:

            self.down_pressed = False

            self.update_player_speed()

        elif key == arcade.key.LEFT:

            self.left_pressed = False

            self.update_player_speed()

        elif key == arcade.key.RIGHT:

            self.right_pressed = False

            self.update_player_speed()



def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()