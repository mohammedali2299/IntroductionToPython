"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and mohammed ali.
"""
########################################################################
# done
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 2)
red_turtle.speed = 307

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', 2)
blue_turtle.speed = 300
size = 10

red_turtle.pen_up()
blue_turtle.pen_up()
red_turtle.pen_down()
blue_turtle.pen_down()

for k in range(8):
    red_turtle.draw_regular_polygon(6,size)


    red_turtle.right(45)
    red_turtle.forward(45)

    size = size - 9

    blue_turtle.draw_circle(4)


    blue_turtle.right(45)
    blue_turtle.forward(45)

    size = size - 9


window.close_on_mouse_click()