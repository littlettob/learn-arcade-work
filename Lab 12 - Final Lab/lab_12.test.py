import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

SCREEN_TITLE= "My Game"

MovementSpeed= 3


class MyGame(arcade.Window):


    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        self.total_time = 0.0
        self.output = "00:00:00"

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        self.center_x = width/2
        self.center_y = height/2

        # backgound
        arcade.set_background_color(arcade.color.BLACK)
        # add Character Image
        self.character_list = arcade.SpriteList()
        self.character = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", .5, center_x= 100, center_y=100)
        self.character_list.append(self.character)

        # set a block
        self.block_list = arcade.SpriteList()
        for counter in range(16):
            block=arcade.Sprite(":resources:images/tiles/grassMid.png", .5)
            block.bottom=0
            block.center_x=0 +64 * counter
            self.block_list.append(block)

        # block mid-air
        for counter in range(13):
            block=arcade.Sprite(":resources:images/tiles/grassHalf_left.png", .5)
            block.bottom=150
            block.center_x=600+ 64 * 2 * counter
            self.block_list.append(block)

        # block mid-air
        for counter in range(13):
            block = arcade.Sprite(":resources:images/tiles/grassHalf_left.png", .5)
            block.bottom = 300
            block.center_x = 100 + 64 * 3 * counter
            self.block_list.append(block)

        # block mid-air middle
        for counter in range(13):
            block = arcade.Sprite(":resources:images/tiles/grassHalf_left.png", .5)
            block.bottom = 450
            block.center_x = 50 + 64 * 4 * counter
            self.block_list.append(block)
        # block mid-air top
        for counter in range(13):
                block = arcade.Sprite(":resources:images/tiles/grassHalf_left.png", .5)
                block.bottom = 650
                block.center_x =75 + 64 * 4 * counter
                self.block_list.append(block)


        # left Stone Block
        for counter in range(13):
            block=arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", .5)
            block.center_x =30
            block.center_y=95+ 64  * counter
            self.block_list.append(block)
        # right Stone Block
            for counter in range(13):
                block = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", .5)
                block.center_x = 970
                block.center_y = 95 + 64 * counter
                self.block_list.append(block)


        # character gravity
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.character,self.block_list, gravity_constant=0.5)

        # jump sound
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        # collect star sound
        self.collect_star_sound = arcade.load_sound(":resources:sounds/coin5.wav")

        # Backgound atmosphere sound
        #self.audio_name = arcade.sound.load_sound("atmosphere.mp3")

        # create a star

        self.star_list = arcade.SpriteList()
        for i in range (50):
            star = arcade.Sprite("star.png")
            star.center_x = random.randint(100, SCREEN_WIDTH)
            star.center_y = random.randint(100, 600)
            self.star_list.append(star)

        # Keep track of the score
        self.score = 0

        # create enemies
        self.enemy_list = arcade.SpriteList()
        for i in range(25):
            enemy = arcade.Sprite(":resources:images/enemies/bee.png",.3)
            enemy.center_x = random.randint(50, SCREEN_WIDTH)
            enemy.center_y = random.randint(800, SCREEN_HEIGHT)
            self.enemy_list.append(enemy)

        self.bullet_list = arcade.SpriteList()

    def on_draw(self):
        #draw the window.
        arcade.start_render()
        # draw the character.
        self.character_list.draw()
        # draw the random star.
        self.star_list.draw()
        #draw the enimies
        self.enemy_list.draw()
        #draw bullet
        self.bullet_list.draw()


        self.block_list.draw()
        #play a sound effect
        #arcade.sound.play_sound(self.audio_name)

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 12,12,arcade.csscolor.BLACK,15,)

        # Output the timer text.
        arcade.draw_text(self.output,
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50,
                         arcade.color.WHITE, 10,
                         anchor_x="center")

    def on_update(self, delta_time):
        self.character_list.update()
        self.physics_engine.update()

        hit_list = arcade.check_for_collision_with_list(self.character,
                                                             self.star_list)
        # loop through each colliding sprite and remove it
        for star in hit_list:
            star.remove_from_sprite_lists()
            arcade.play_sound(self.collect_star_sound)

            self.score += 1
        self.total_time += delta_time

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Calculate 100s of a second
        seconds_100s = int((self.total_time - seconds) * 100)

        # Figure out our output
        self.output = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"

        for enemy in self.enemy_list:
            odds = 200
            # Adjust odds based on delta-time
            adj_odds = int(odds * (1 / 60) / delta_time)

            if random.randrange(adj_odds) == 0:
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", .4)
                bullet.center_x = enemy.center_x
                bullet.angle = -90
                bullet.top = enemy.bottom
                bullet.change_y = -2
                self.bullet_list.append(bullet)

            # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()




    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.character.change_y = 10
            arcade.play_sound(self.jump_sound)

        elif key == arcade.key.DOWN:
            self.character.change_y = -MovementSpeed
        elif key == arcade.key.LEFT:
            self.character.change_x = -MovementSpeed
        elif key == arcade.key.RIGHT:
            self.character.change_x = MovementSpeed

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.character.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.character.change_y = 0


if __name__ == "__main__":
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()