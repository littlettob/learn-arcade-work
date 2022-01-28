# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(900, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Drawing sun
arcade.draw_arc_filled(200, 550, 80,80,
                        arcade.color.YELLOW, 0, 360)
# 2 Ray on the left
arcade.draw_line(200, 550, 500, 550, arcade.color.YELLOW, 3)
arcade.draw_line(200, 550, 400, 450, arcade.color.YELLOW, 3)
# 2 Ray on the right
arcade.draw_line(200, 550, 50, 500, arcade.color.YELLOW, 3)
arcade.draw_line(200, 550, 50, 600, arcade.color.YELLOW, 3)

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 900, 100, 0, arcade.color.BITTER_LIME)

# Draw Cloud Left
arcade.draw_circle_filled(60, 470, 40, arcade.color.WHITE)
arcade.draw_circle_filled(90, 480, 40, arcade.color.WHITE)
arcade.draw_circle_filled(130, 475, 45, arcade.color.WHITE)

# Draw Cloud Middle
arcade.draw_circle_filled(230, 550, 40, arcade.color.WHITE)
arcade.draw_circle_filled(260, 580, 40, arcade.color.WHITE)
arcade.draw_circle_filled(280, 560, 45, arcade.color.WHITE)

# Draw Cloud Right
arcade.draw_circle_filled(700, 550, 40, arcade.color.WHITE)
arcade.draw_circle_filled(720, 580, 40, arcade.color.WHITE)
arcade.draw_circle_filled(760, 560, 45, arcade.color.WHITE)


#Tree Trunk right
point_list = ((30, 100),
              (40, 300),
              (50, 300),
              (60, 100))
arcade.draw_polygon_filled(point_list, arcade.color.BROWN)
#Tree Leaf right
arcade.draw_arc_filled(40,300,120,80,
                        arcade.color.FOREST_GREEN, 0, 360)
arcade.draw_arc_filled(40,330,130,80,
                        arcade.color.FOREST_GREEN, 0, 360)
arcade.draw_arc_filled(40,340,110,100,
                        arcade.color.FOREST_GREEN, 0, 360)
arcade.draw_arc_filled(50,390,60,90,
                        arcade.color.FOREST_GREEN, 0, 360)


#Tree Trunk left
point_list = ((830, 100),
              (840, 300),
              (850, 300),
              (860, 100))
arcade.draw_polygon_filled(point_list, arcade.color.BROWN)
#Tree Leaf left
arcade.draw_arc_filled(840,300,100,80,
                        arcade.color.FOREST_GREEN, 0, 360)
arcade.draw_arc_filled(840,330,140,80,
                        arcade.color.FOREST_GREEN, 0, 360)
arcade.draw_arc_filled(840,340,160,100,
                        arcade.color.FOREST_GREEN, 0, 360)
arcade.draw_arc_filled(850,390,100,90,
                        arcade.color.FOREST_GREEN, 0, 360)


# Car Body
arcade.draw_arc_filled(200,115,140,60,
                        arcade.color.BLUE, 0, 180)
arcade.draw_arc_filled(200,130,80,60,
                        arcade.color.BLUE, 0, 180)
# Car Glass left
arcade.draw_arc_filled(200,130,52,37,
                        arcade.color.WHITE, 0,90)
# Car Glass right
arcade.draw_arc_filled(195,130,55,35,
                       arcade.color.WHITE, 90,180)
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

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
