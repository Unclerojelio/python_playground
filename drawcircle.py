"""
drawcircle.py
A python program that draws a circle
From the book, "Python Playground"
Author: Mahesh Venkitachalam
Website: electronut.in
Modified by: Roger Banks (roger_banks@mac.com)
"""

import math
import turtle

# draw the circle using turtle
def drawCircleTurtle(x, y, r):
	turtle.up()
	turtle.setpos(x + r, y)
	turtle.down()
	
	# draw the circle
	for i in range(0, 365, 5):
		a = math.radians(i)
		turtle.setpos(x + r*math.cos(a),y + r*math.sin(a))
	
drawCircleTurtle(100, 100, 50)
turtle.mainloop()