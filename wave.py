import math
import turtle
import tkinter as tk

def main():
	pen = turtle.Turtle()
	screen = turtle.Screen()
	n_waves = 10
	wave_height = 10
	world_capacity = (2 * math.pi) * n_waves

	pen.color("green")
	screen.tracer(1, 1)
	screen.setworldcoordinates(0, -(wave_height), world_capacity, wave_height)

	theta = 1

	while theta < world_capacity:
		pen.goto(theta, trig("log", theta) * math.pi * trig("sin", theta))
		theta += 0.1

	screen.exitonclick()


def trig(trig_op, theta):
	return eval("math." + trig_op + "(" + str(theta) + ")")


def sigmoid(x):
	return 1 / (1 + math.e ** -(x))


def ReLU(x):
	return max(0, x)


if __name__ == "__main__":
	main()