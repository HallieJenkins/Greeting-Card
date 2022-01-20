# Name: Hallie Jenkins
# greetingcard.py

# Purpose: An animated holiday greeting card
# Certification of Authenticity: I certify that this code is entirely
# my own work.

# Input: User clicks mouse to cause action
# Output: Animation

from graphics import *
from random import *


def card():
    win = GraphWin("Happy Thanksgiving!",695, 600, autoflush=False)
    win.setBackground(color_rgb(145, 222, 255))
# All variables that end in "_colors" are lists that store colors for
# their indicated image to utilize
    # Sky List
    sky_colors = [color_rgb(145, 222, 255), color_rgb(150,227,255)]

    # Grass list
    grass_colors = [color_rgb(66, 181, 27), color_rgb(189, 111, 38),
                    color_rgb(163, 63, 55)]

    # Trunk list
    trunk_colors = [color_rgb(119,70,65),color_rgb(122,55,9),
                    color_rgb(133,85,56)]

    # Leaf list
    leaf_colors = [color_rgb(189, 111, 38),color_rgb(163, 63, 55),
                   color_rgb(79, 55, 43)]

    # Cloud list
    cloud_colors = [color_rgb(255, 255, 255),color_rgb(237, 239, 240)]

    # Table List
    table_colors = [color_rgb(191,185,168),color_rgb(160,139,117)]

    # Pumpkin list
    pumpkin_colors = [color_rgb(255,102,0), color_rgb(255,120,0)]

# All variables that end in "_square" are 5 pixel x 5 pixel Rectangles
# that when combined create the image indicated in the comment above
# the loop

# All variables that end in "_color_value" are random numbers within
# the length of their image's color lists that decide which color
# from the list to assign to each rectangle to create the image

    # Sky loop
    for x in range(0,695,5):
        for y in range(0,600,5):
            sky_square = Rectangle(Point(x,y),Point(x+5,y+5))
            sky_color_value = randrange(0,2)
            sky_square.setFill(sky_colors[sky_color_value])
            sky_square.setOutline(sky_colors[sky_color_value])
            sky_square.draw(win)

    # Cloud Loops
    for x in range(20,100,5):
        for y in range(20,80,5):
            cloud_square = Rectangle(Point(x,y),Point(x+5,y+5))
            cloud_color_value = randrange(0,2)
            cloud_square.setFill(cloud_colors[cloud_color_value])
            cloud_square.setOutline(cloud_colors[cloud_color_value])
            cloud_square.draw(win)
    for x in range(595,675,5):
        for y in range(20,80,5):
            cloud_square = Rectangle(Point(x,y),Point(x+5,y+5))
            cloud_color_value = randrange(0,2)
            cloud_square.setFill(cloud_colors[cloud_color_value])
            cloud_square.setOutline(cloud_colors[cloud_color_value])
            cloud_square.draw(win)

    for x in range(535,615,5):
        for y in range(120,180,5):
            cloud_square = Rectangle(Point(x,y),Point(x+5,y+5))
            cloud_color_value = randrange(0,2)
            cloud_square.setFill(cloud_colors[cloud_color_value])
            cloud_square.setOutline(cloud_colors[cloud_color_value])
            cloud_square.draw(win)
    for x in range(50,130,5):
        for y in range(120,180,5):
            cloud_square = Rectangle(Point(x,y),Point(x+5,y+5))
            cloud_color_value = randrange(0,2)
            cloud_square.setFill(cloud_colors[cloud_color_value])
            cloud_square.setOutline(cloud_colors[cloud_color_value])
            cloud_square.draw(win)
# 455
    for x in range(455,535,5):
        for y in range(30,90,5):
            cloud_square = Rectangle(Point(x,y),Point(x+5,y+5))
            cloud_color_value = randrange(0,2)
            cloud_square.setFill(cloud_colors[cloud_color_value])
            cloud_square.setOutline(cloud_colors[cloud_color_value])
            cloud_square.draw(win)

    # Grass loop
    for x in range(0,695,5):
        for y in range(410,600,5):
            grass_square = Rectangle(Point(x,y),Point(x+5,y+5))
            grass_color_value = randrange(0,3)
            grass_square.setFill(grass_colors[grass_color_value])
            grass_square.setOutline(grass_colors[grass_color_value])
            grass_square.draw(win)

    # Trunk Loop
    for x in range(331,359,5):
        for y in range(295,500,5):
            trunk_square = Rectangle(Point(x,y), Point(x+5, y+5))
            trunk_color_value = randrange(0,3)
            trunk_square.setFill(trunk_colors[trunk_color_value])
            trunk_square.setOutline(trunk_colors[trunk_color_value])
            trunk_square.draw(win)

    # Polygon Tree Loop
    for x in range(250, 450, 5):
        for y in range(105,300, 5):
            leaf_square = Polygon(Point(x, y),
                                  Point(x + 5, y + 5),
                                  Point(x + 10, y),
                                  Point(x + 5, y - 5))
            leaf_color_value = randrange(0, 3)
            leaf_square.setFill(leaf_colors[leaf_color_value])
            leaf_square.setOutline(leaf_colors[leaf_color_value])
            leaf_square.draw(win)

# The two angle loops cut off the corners of the tree by covering them
# in objects the same color as the sky to make the tree appear more
# tree-like

    # Bottom left tree angle
    for y in range(225, 300, 5):
        for x in range(y-70, y, 5):
            leaf_square = Rectangle(Point(x, y), Point(x+5, y + 5))
            leaf_color_value = randrange(0, 2)
            leaf_square.setFill(sky_colors[leaf_color_value])
            leaf_square.setOutline(sky_colors[leaf_color_value])
            leaf_square.draw(win)

    # Top Right tree angle
    for x in range(400, 470, 5):
        for y in range(x-365, x-295, 5):
            leaf_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            leaf_color_value = randrange(0, 2)
            leaf_square.setFill(sky_colors[leaf_color_value])
            leaf_square.setOutline(sky_colors[leaf_color_value])
            leaf_square.draw(win)

        # Table Leg
        table_leg = Rectangle(Point(100,390),Point(100,430))
        table_leg_2 = Rectangle(Point(200,390),Point(200,430))
        table_leg.draw(win)
        table_leg_2.draw(win)

# Table
    # Table Loop
    for x in range(95,205,5):
        for y in range(390,395,5):
            table_square = Rectangle(Point(x, y), Point(x + 5,
                                                        y + 5))
            table_color_value = randrange(0,2)
            table_square.setFill(table_colors[table_color_value])
            table_square.setOutline(table_colors[table_color_value])
            table_square.draw(win)
    # Bench Loop
    for x in range(90, 210, 5):
        for y in range(405, 410, 5):
            bench_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            bench_color_value = randrange(0, 2)
            bench_square.setFill(table_colors[bench_color_value])
            bench_square.setOutline(table_colors[bench_color_value])
            bench_square.draw(win)

# This loop draws a group of corn stalks square-by-square to make
# them appear to be growing up from the ground
    # Corn Stalk
    for y in range(425, 325, -5):
        for x in range(525,625,30):

            stalk_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            stalk_square.setFill("green3")
            stalk_square.setOutline("green4")
            stalk_square.draw(win)
        update(5)

# Creates instructions for the user
    instructions = Text(Point(347.5, 8), "Click the window")
    instructions.draw(win)
    win.getMouse()
    instructions.undraw()
# All loops labeled "Corn #" and "Husk #" draw ears of corn and their
# husks onto the previously created stalks

    # Corn 1
    for x in range(525, 509, -5):
        for y in range(x - 180, x - 170, 5):
            corn_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            # corn_color_value = randrange(0, 2)
            corn_square.setFill("yellow2")
            corn_square.setOutline("yellow3")
            corn_square.draw(win)
            update(20)

    # Husk 1
    for x in range(525, 509, -5):
        for y in range(x - 175, x - 165, 5):
            corn_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            # leaf_color_value = randrange(0, 2)
            corn_square.setFill("green3")
            corn_square.setOutline("green4")
            corn_square.draw(win)
            update(20)

    # Corn 2
    for x in range(555, 539, -5):
        for y in range(x - 180, x - 170, 5):
            corn_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            # leaf_color_value = randrange(0, 2)
            corn_square.setFill("yellow2")
            corn_square.setOutline("yellow3")
            corn_square.draw(win)
            update(20)

    # Husk 2
    for x in range(555, 539, -5):
        for y in range(x - 175, x - 165, 5):
            corn_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            # leaf_color_value = randrange(0, 2)
            corn_square.setFill("green3")
            corn_square.setOutline("green4")
            corn_square.draw(win)
            update(20)

    # Corn 3
    for x in range(585, 569, -5):
        for y in range(x - 240, x - 230, 5):
            corn_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            # leaf_color_value = randrange(0, 2)
            corn_square.setFill("yellow2")
            corn_square.setOutline("yellow3")
            corn_square.draw(win)
            update(20)
    # Husk 3
    for x in range(585, 569, -5):
        for y in range(x - 235, x - 225, 5):
            corn_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            # leaf_color_value = randrange(0, 2)
            corn_square.setFill("green3")
            corn_square.setOutline("green4")
            corn_square.draw(win)
            update(20)

    # Corn 4
    for x in range(615, 599, -5):
        for y in range(x - 240, x - 230, 5):
            corn_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            # leaf_color_value = randrange(0, 2)
            corn_square.setFill("yellow2")
            corn_square.setOutline("yellow3")
            corn_square.draw(win)
            update(20)
    # Husk 4
    for x in range(615, 599, -5):
        for y in range(x - 235, x - 225, 5):
            corn_square = Rectangle(Point(x, y),
                                    Point(x + 5, y + 5))
            # leaf_color_value = randrange(0, 2)
            corn_square.setFill("green3")
            corn_square.setOutline("green4")
            corn_square.draw(win)
            update(20)

    # This loop draws a pumpkin to place on the picnic table
    for x in range(140, 160, 5):
        for y in range(375, 390, 5):
            pumpkin_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            pumpkin_color_value = randrange(0, 2)
            pumpkin_square.setFill(pumpkin_colors
                                   [pumpkin_color_value])
            pumpkin_square.setOutline(pumpkin_colors
                                      [pumpkin_color_value])
            pumpkin_square.draw(win)
    stem = Rectangle(Point(152, 375), Point(148, 370))
    stem.setFill("green")
    stem.setOutline("green")
    stem.draw(win)

# The following loops draw a pilgrim and his clothing. What each loop
# draws is indicated in the comment prior to each one

    black_colors = [color_rgb(0, 0, 0), color_rgb(10, 10, 10)]

    # Hat Brim
    for x in range(45, 80, 5):
        for y in range(335, 340, 5):
            hat_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            black_color_value = randrange(0, 2)
            hat_square.setFill(black_colors[black_color_value])
            hat_square.setOutline(black_colors[black_color_value])
            hat_square.draw(win)

    # Hat Top
    for x in range(50, 75, 5):
        for y in range(315, 335, 5):
            hat_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            black_color_value = randrange(0, 2)
            hat_square.setFill(black_colors[black_color_value])
            hat_square.setOutline(black_colors[black_color_value])
            hat_square.draw(win)

    belt_color_list = [color_rgb(160, 82, 45), color_rgb(139, 69, 19)]

    # Hat Belt
    for x in range(50, 75, 5):
        for y in range(330, 335, 5):
            hat_belt_square = Rectangle(Point(x, y), Point(x + 5,
                                                           y + 5))
            hat_belt_color_value = randrange(0, 2)
            hat_belt_square.setFill(belt_color_list[
                                        hat_belt_color_value])
            hat_belt_square.setOutline(belt_color_list[
                                           hat_belt_color_value])
            hat_belt_square.draw(win)
    hat_buckle = Rectangle(Point(60, 330), Point(65, 335))
    hat_buckle.setFill("gold")
    hat_buckle.setOutline("goldenrod")
    hat_buckle.draw(win)

    # Hair
    hair_colors = [color_rgb(133, 74, 8), color_rgb(138, 76, 6),
                   color_rgb(150, 82, 3)]
    # Hair left
    for x in range(45, 50, 5):
        for y in range(340, 355, 5):
            hair_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            hair_color_value = randrange(0, 3)
            hair_square.setFill(hair_colors[hair_color_value])
            hair_square.setOutline(hair_colors[hair_color_value])
            hair_square.draw(win)

    # Hair Right
    for x in range(75, 80, 5):
        for y in range(340, 355, 5):
            hair_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            hair_color_value = randrange(0, 3)
            hair_square.setFill(hair_colors[hair_color_value])
            hair_square.setOutline(hair_colors[hair_color_value])
            hair_square.draw(win)

    # Face
    skin_colors = [color_rgb(255, 220, 177), color_rgb(254, 224, 196)]
    for x in range(50, 75, 5):
        for y in range(340, 360, 5):
            skin_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            skin_color_value = randrange(0, 1)
            skin_square.setFill(skin_colors[skin_color_value])
            skin_square.setOutline(skin_colors[skin_color_value])
            skin_square.draw(win)

    # Eyes
    left_eye = Rectangle(Point(55.5, 345), Point(58, 347.5))
    left_eye.setFill("green")
    left_eye.setOutline("green")
    left_eye.draw(win)

    right_eye = Rectangle(Point(67.5, 345), Point(70, 347.5))
    right_eye.setFill("green")
    right_eye.setOutline("green")
    right_eye.draw(win)

    # Nose
    nose = Rectangle(Point(62.75, 348), Point(63.25, 352))
    nose.setFill("pink")
    nose.setOutline("pink")
    nose.draw(win)

    # Mouth
    mouth_center = Rectangle(Point(58, 356.5), Point(67.5, 357.5))
    mouth_center.setFill("salmon")
    mouth_center.setOutline("salmon")
    mouth_center.draw(win)

    # Neck
    for x in range(55, 70, 5):
        for y in range(360, 365, 5):
            skin_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            skin_color_value = randrange(0, 1)
            skin_square.setFill(skin_colors[skin_color_value])
            skin_square.setOutline(skin_colors[skin_color_value])
            skin_square.draw(win)

    # Shoulders
    for x in range(45, 80, 5):
        for y in range(365, 370, 5):
            clothes_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            clothes_color_value = randrange(0, 2)
            clothes_square.setFill("white")
            clothes_square.setOutline(black_colors[clothes_color_value])
            clothes_square.draw(win)

    # Body
    for x in range(50, 75, 5):
        for y in range(370, 395, 5):
            clothes_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            clothes_color_value = randrange(0, 2)
            clothes_square.setFill(black_colors[clothes_color_value])
            clothes_square.setOutline(black_colors[clothes_color_value])
            clothes_square.draw(win)

    # Left Arm
    for x in range(80, 85, 5):
        for y in range(370, 395, 5):
            clothes_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            clothes_color_value = randrange(0, 2)
            clothes_square.setFill(black_colors[clothes_color_value])
            clothes_square.setOutline(black_colors[clothes_color_value])
            clothes_square.draw(win)

    # Left Hand
    left_hand = Rectangle(Point(80, 395), Point(85, 400))
    left_hand.setFill(skin_colors[0])
    left_hand.draw(win)

    # Pants
    for x in range(50, 75, 5):
        for y in range(395, 410, 5):
            clothes_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            clothes_color_value = randrange(0, 2)
            clothes_square.setFill(black_colors[clothes_color_value])
            clothes_square.setOutline(black_colors[clothes_color_value])
            clothes_square.draw(win)

    # Belt
    for x in range(50, 75, 5):
        for y in range(395, 400, 5):
            belt_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            belt_color_value = randrange(0, 2)
            belt_square.setFill(belt_color_list[belt_color_value])
            belt_square.setOutline(belt_color_list[belt_color_value])
            belt_square.draw(win)
    belt_buckle = Rectangle(Point(60, 395), Point(65, 400))
    belt_buckle.setFill("gold")
    belt_buckle.setOutline("goldenrod")
    belt_buckle.draw(win)

    # Left Leg
    for x in range(50, 60, 5):
        for y in range(405, 430, 5):
            clothes_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            clothes_color_value = randrange(0, 2)
            clothes_square.setFill(black_colors[clothes_color_value])
            clothes_square.setOutline(black_colors[clothes_color_value])
            clothes_square.draw(win)

    # Right Leg
    for x in range(65, 75, 5):
        for y in range(405, 430, 5):
            clothes_square = Rectangle(Point(x, y), Point(x + 5, y + 5))
            clothes_color_value = randrange(0, 2)
            clothes_square.setFill(black_colors[clothes_color_value])
            clothes_square.setOutline(black_colors[clothes_color_value])
            clothes_square.draw(win)

    # Right Arm
    point_1 = Point(40, 345)
    point_2 = Point(45, 345)
    point_3 = Point(45, 370)
    point_4 = Point(40, 370)
    arm = Polygon(point_1, point_2, point_3, point_4)
    arm.setFill("black")

    # Right Hand
    point_1h = Point(40,340)
    point_2h = Point(45,340)
    point_3h = Point(45,345)
    point_4h = Point(40,345)
    hand = Polygon(point_1h,point_2h, point_3h, point_4h)
    hand.setFill(skin_colors[0])

    # This creates greeting to say "Happy Thanksgiving!"
    greeting = Text(Point(277.5, 50), "Happy Thanksgiving!")
    greeting.setSize(30)
    greeting.setTextColor("brown")
    greeting.setStyle("bold")
    greeting.setFace("courier")
    greeting.draw(win)

    # Updates instruction to let the user know to click when they're
    # ready to close the window
    instructions.setText("Click to close")
    instructions.draw(win)

# This while loop makes the pilgrim wave until the user clicks to
# close the window by repeatedly drawing the arm, undrawing the arm
# moving the points to new positions and drawing it again with the new
# point positions before updating the window
    while not win.checkMouse():
        # The points that make up the arm and hand are reset at the
        # beginning of the while loop everytime it runs
        point_1 = Point(40, 345)
        point_2 = Point(45, 345)
        point_3 = Point(45, 370)
        point_4 = Point(40, 370)

        point_1h = Point(40, 340)
        point_2h = Point(45, 340)
        point_3h = Point(45, 345)
        point_4h = Point(40, 345)

        # This loop tilts the arm to the left edge of the window
        for i in range(10):
            arm.undraw()
            hand.undraw()

            point_1.move(-.1, 0)
            point_2.move(-.1, 0)

            point_1h.move(-.1,0)
            point_2h.move(-.1,0)
            point_3h.move(-.1,0)
            point_4h.move(-.1,0)

            arm = Polygon(point_1, point_2, point_3,
                          point_4)
            arm.setFill("black")
            arm.draw(win)

            hand = Polygon(point_1h, point_2h, point_3h, point_4h)
            hand.setFill(skin_colors[0])
            hand.draw(win)

            update(200)

        # This loop tilts the arm back to an upright position
        for j in range(10):
            arm.undraw()
            hand.undraw()

            point_1.move(.1, 0)
            point_2.move(.1, 0)

            point_1h.move(.1,0)
            point_2h.move(.1,0)
            point_3h.move(.1,0)
            point_4h.move(.1,0)

            arm = Polygon(point_1, point_2, point_3,
                          point_4)
            arm.setFill("black")
            arm.draw(win)

            hand = Polygon(point_1h, point_2h, point_3h, point_4h)
            hand.setFill(skin_colors[0])
            hand.draw(win)

            update(200)

        # This loop tilts the arm toward the right edge of the window
        for k in range(10):
            arm.undraw()
            hand.undraw()

            point_1.move(.1, 0)
            point_2.move(.1, 0)

            point_1h.move(.1,0)
            point_2h.move(.1,0)
            point_3h.move(.1,0)
            point_4h.move(.1,0)

            arm = Polygon(point_1, point_2, point_3,
                          point_4)
            arm.setFill("black")
            arm.draw(win)

            hand = Polygon(point_1h, point_2h, point_3h, point_4h)
            hand.setFill(skin_colors[0])
            hand.draw(win)

            update(200)

    win.checkMouse()
    win.close()


card()
