import arcade

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.

        self.set_mouse_visible(False)
        #x y and speed
        self.a_x = 100
        self.a_y = 200
        self.a_speed = 200

        # add Character Image
        self.character= arcade.Sprite("spaceship.png", center_x=50, center_y=50)
        # set all false
        self.right= False
        self.left = False
        self.up = False
        self.down = False
        # Backgound atmosphere sound
        self.audio_name = arcade.sound.load_sound("atmosphere.mp3")

    def on_draw(self):
        arcade.start_render()
        # draw the window.
        self.character.draw()
        # play a sound effect
        arcade.sound.play_sound(self.audio_name)

    def on_update(self, delta_time):
        if self.right:
            self.character.turn_right(2)
        if self.left:
            self.character.turn_left(2)
        if self.up:
            pass
        if self.down:
            pass
        self.character.update()
        #self.character.set_position(self.a_x, self.a_y)

    def on_key_press(self, symbol, modifiers):
            #the user presses a key
        if symbol == arcade.key.RIGHT:
            self.character.strafe(.5)
            self.right=True
        if symbol == arcade.key.LEFT:
            self.character.strafe(.5)
            self.left=True
        if symbol == arcade.key.UP:
            self.character.strafe(.5)
            self.up=True
        if symbol == arcade.key.DOWN:
            self.character.strafe(.5)
            self.down=True

    def on_key_release(self, symbol, modifiers):
        # a user releases a key
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
