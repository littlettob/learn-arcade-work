""" Lab 7 - User Control """

import arcade

class MyGame(arcade.Window):


    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.

        self.set_mouse_visible(False)
        self.a_x = 100
        self.a_y = 200
        self.a_speed = 200
        # backgound
        arcade.set_background_color(arcade.color.BLACK)
        # add Character Image
        self.character= arcade.Sprite("spaceship.png", center_x=50, center_y=50)
        # Backgound atmosphere sound
        self.audio_name = arcade.sound.load_sound("atmosphere.mp3")

        # set all false
        self.right= False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        #draw the window.
        arcade.start_render()
        self.character.draw()
        #play a sound effect
        arcade.sound.play_sound(self.audio_name)

    def on_update(self, delta_time):
        #the user presses a key
        if self.right:
            self.a_x += self.a_speed * delta_time
        if self.left:
            self.a_x -= self.a_speed * delta_time
        if self.up:
            self.a_y += self.a_speed * delta_time
        if self.down:
            self.a_y -= self.a_speed * delta_time
        self.character.set_position(self.a_x, self.a_y)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right=True
        if symbol == arcade.key.LEFT:
            self.left=True
        if symbol == arcade.key.UP:
            self.up=True
        if symbol == arcade.key.DOWN:
            self.down=True

    def on_key_release(self, symbol, modifiers):
        # user releases a key
        if symbol == arcade.key.RIGHT:
            self.right=False
        if symbol == arcade.key.LEFT:
            self.left=False
        if symbol == arcade.key.UP:
            self.up=False
        if symbol == arcade.key.DOWN:
            self.down=False
MyGame(600,600,"My Game")
arcade.run()
