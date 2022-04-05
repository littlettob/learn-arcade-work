import arcade
import random

class MyGame(arcade.Window):


    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        self.center_x = width/2
        self.center_y = height/2

        # backgound
        arcade.set_background_color(arcade.color.BLACK)
        # add Character Image
        self.character_list = arcade.SpriteList()
        self.character = arcade.Sprite("spaceship.png", 1.5)
        self.character_list.append(self.character)


        # Backgound atmosphere sound
        self.audio_name = arcade.sound.load_sound("atmosphere.mp3")

        # create a star

        self.star_list = arcade.SpriteList()
        for i in range (100):
            star = arcade.Sprite("star.png")
            star.center_x=random.randint(0,600)
            star.center_y = random.randint(0, 600)
            self.star_list.append(star)


    def on_draw(self):
        #draw the window.
        arcade.start_render()
        self.character_list.draw()
        self.star_list.draw()
        #play a sound effect
        arcade.sound.play_sound(self.audio_name)

    def on_update(self, delta_time):
        self.character_list.update()

        hit_list = arcade.check_for_collision_with_list(self.character,
                                                             self.star_list)
        # loop through each colliding sprite and remove it
        for star in hit_list:
            star.remove_from_sprite_lists()

    def on_mouse_motion(self, x, y, dx, dy):
        self.character.center_x = x
        self.character.center_y = y


MyGame(600,600,"My Game")
arcade.run()