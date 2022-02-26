# Lab 5 Loop Due 2/24/2022
import arcade

COLUMN_SPACING = 10
ROW_SPACING = 10
LEFT_MARGIN = 5
BOTTOM_MARGIN = 5



def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    # Loop for each column
    for row in range(30):
        # Loop for each column
        # Change the number of columns depending on the row we are in
        for column in range(30):
            # Calculate our location
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN

            # Draw the item
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    # Loop for each column
    for row in range(30):
        # Loop for each column
        # Change the number of columns depending on the row we are in
        for column in range(30):
            # Calculate our location
            x = 300 + column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

         #   if x % 10==0:

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


    pass


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    for row in range(30):
        # Loop for each column
        # Change the number of columns depending on the row we are in
        for column in range(30):
            # Calculate our location
            x = 900 + column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

    pass


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    for row in range(30):
        # Loop for each column
        # Change the number of columns depending on the row we are in
        for column in range(30):
            # Calculate our location
            x = 600 + column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
    pass


def draw_section_5():
    for column in range(30):
        # Loop for each column
        # Change the number of columns depending on the row we are in
        for row in range(column):
            # Calculate our location
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = 300 + row * ROW_SPACING + BOTTOM_MARGIN

            # Draw the item
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    pass


def draw_section_6():
    for row in range(30):
        # Loop for each column
        # Change the number of columns depending on the row we are in
        for column in range(30-row):
            # Calculate our location
            x = 300 + column * COLUMN_SPACING + LEFT_MARGIN
            y = 300 + row * ROW_SPACING + BOTTOM_MARGIN

            # Draw the item
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    pass


def draw_section_7():
    for row in range(30):
        # Loop for each column
        # Change the number of columns depending on the row we are in
        for column in range(row):
            # Calculate our location
            x = 600 + column * COLUMN_SPACING + LEFT_MARGIN
            y = 300 + row * ROW_SPACING + BOTTOM_MARGIN

            # Draw the item
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    pass


def draw_section_8():
    for column in range(30):
        # Loop for each column
        # Change the number of columns depending on the row we are in
        for row in range(30-(column+1),30):
            # Calculate our location
            x = 900 + column * COLUMN_SPACING + LEFT_MARGIN
            y = 300 + row * ROW_SPACING + BOTTOM_MARGIN

            # Draw the item
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    pass


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()