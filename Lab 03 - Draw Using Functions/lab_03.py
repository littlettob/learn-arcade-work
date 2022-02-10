import arcade

# Constants - variables that do not change
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


def draw_background():
# This function draws the background, and the sky and ground.

    # Draw the sky in the top two-thirds
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      SCREEN_HEIGHT * (1 / 6),
                                      arcade.color.SKY_BLUE)

    # Draw the ground in the bottom third
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT / 6,
                                      0,
                                      arcade.color.BITTER_LIME)
def draw_cload(x, y):
    """
    This function draws cload using cỉcle
    """
    # Draw Cloud Left
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 45, arcade.color.WHITE)

    # Draw Cloud Middle
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 45, arcade.color.WHITE)
    # Draw Cloud Right
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 45, arcade.color.WHITE)


def draw_sun(x, y):
    """
    Draw a sun using arcs.
    """
    arcade.draw_arc_filled(x, 15 + y, 80, 80,
                           arcade.color.YELLOW, 0, 360)


def draw_sunray(x, y):
    # 2 Ray on the left
    arcade.draw_line(x -10, y +5, 500, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(x +10, y-5, 400, 450, arcade.color.YELLOW, 3)
    # 2 Ray on the right
    arcade.draw_line(x+10, y -5, 50, 500, arcade.color.YELLOW, 3)
    arcade.draw_line(x -10 ,y+5, 50, 600, arcade.color.YELLOW, 3)
def draw_cload(x, y):
        """
        This function draws cload using cỉcle
        """
        # Draw Cloud Left
        arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x, y, 45, arcade.color.WHITE)

        # Draw Cloud Middle
        arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x, y, 45, arcade.color.WHITE)
        # Draw Cloud Right
        arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x, y, 45, arcade.color.WHITE)

def on_draw(delta_time):
    """
    This is the main program.
    """
    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()
    #drawing background
    draw_background()
    # 2 Sun
    draw_sun(200, 550)


    # 2 Ray on the left
    draw_sunray(200, 550)
    draw_sunray(200, 550)
    # 2 Ray on the right
    draw_sunray(200, 550)
    draw_sunray(200, 550)

    draw_sun(on_draw.sun1_x, 550)

    # Call our drawing cload left
    draw_cload(60, 470)
    draw_cload(90, 480)
    draw_cload(130, 475)
    # Call our drawing cload middle
    draw_cload(230, 550)
    draw_cload(260, 580)
    draw_cload(280, 560)
    # Call our drawing cload right
    draw_cload(700, 550)
    draw_cload(720, 580)
    draw_cload(760, 560)

    # Tree Trunk right
    point_list = ((30, 100),
                  (40, 300),
                  (50, 300),
                  (60, 100))
    arcade.draw_polygon_filled(point_list, arcade.color.BROWN)
    # Tree Leaf right
    arcade.draw_arc_filled(40, 300, 120, 80,
                           arcade.color.FOREST_GREEN, 0, 360)
    arcade.draw_arc_filled(40, 330, 130, 80,
                           arcade.color.FOREST_GREEN, 0, 360)
    arcade.draw_arc_filled(40, 340, 110, 100,
                           arcade.color.FOREST_GREEN, 0, 360)
    arcade.draw_arc_filled(50, 390, 60, 90,
                           arcade.color.FOREST_GREEN, 0, 360)

    # Tree Trunk left
    point_list = ((830, 100),
                  (840, 300),
                  (850, 300),
                  (860, 100))
    arcade.draw_polygon_filled(point_list, arcade.color.BROWN)
    # Tree Leaf left
    arcade.draw_arc_filled(840, 300, 100, 80,
                           arcade.color.FOREST_GREEN, 0, 360)
    arcade.draw_arc_filled(840, 330, 140, 80,
                           arcade.color.FOREST_GREEN, 0, 360)
    arcade.draw_arc_filled(840, 340, 160, 100,
                           arcade.color.FOREST_GREEN, 0, 360)
    arcade.draw_arc_filled(850, 390, 100, 90,
                           arcade.color.FOREST_GREEN, 0, 360)

    # Car Body
    arcade.draw_arc_filled(200, 115, 140, 60,
                           arcade.color.BLUE, 0, 180)
    arcade.draw_arc_filled(200, 130, 80, 60,
                           arcade.color.BLUE, 0, 180)
    # Car Glass left
    arcade.draw_arc_filled(200, 130, 52, 37,
                           arcade.color.WHITE, 0, 90)
    # Car Glass right
    arcade.draw_arc_filled(195, 130, 55, 35,
                           arcade.color.WHITE, 90, 180)
    # Car Glass tire left
    arcade.draw_circle_filled(235, 115, 15, arcade.color.BLACK)
    # Car Glass tire right
    arcade.draw_circle_filled(165, 115, 15, arcade.color.BLACK)

    # House right side
    arcade.draw_polygon_filled([[300, 100],
                                [600, 100],
                                [600, 300],
                                [450, 450],
                                [300, 300]],
                               arcade.color.GRAY_BLUE)
    # House Left side
    arcade.draw_polygon_filled([[600, 100],
                                [800, 100],
                                [800, 300],
                                [600, 300]],
                               arcade.color.GRAY)
    # House Roof
    arcade.draw_polygon_filled([[450, 450],
                                [600, 300],
                                [800, 300],
                                [650, 450],
                                [620, 450],
                                [620, 470],
                                [600, 470],
                                [600, 450],
                                [450, 450]],
                               arcade.color.RED_BROWN)
    # Window
    arcade.draw_rectangle_filled(450, 250, 88, 99, arcade.color.BONE)
    arcade.draw_rectangle_filled(450, 250, 70, 90, arcade.color.SKY_BLUE)
    # Door
    arcade.draw_rectangle_filled(700, 150, 65, 100, arcade.color.ORANGE_RED)
    # Door Knob
    arcade.draw_circle_filled(720, 150, 5, arcade.color.BLACK)




    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.sun1_x += 10


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.sun1_x = 3


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 20th of a second.
    arcade.schedule(on_draw, 1 / 20)
    arcade.run()


# Call the main function to get the program started.
main()