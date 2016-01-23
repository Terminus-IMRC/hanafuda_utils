#!/usr/bin/env python3

# Copyright 2016 Sugizaki Yukimasa
# This software is licensed under CC BY-SA 4.0.

IMAGE_WIDTH = 64
IMAGE_HEIGHT = 102

def exit_program(x = None):
	exit(0)

import sys

if len(sys.argv) != 2:
	print("Usage: %s '[card numbers]'" % (sys.argv[0]))
	exit_program()

import tkinter
from PIL import Image, ImageTk

nums = [(int(j / 4) + 1, j % 4 + 1) for j in [int(i) for i in sys.argv[1].split()]]
length = len(nums)

photos = [None for i in range(length)]

root = tkinter.Tk()
root.bind("<KeyPress-q>", exit_program)
root.geometry('%dx%d' % (IMAGE_WIDTH * length, IMAGE_HEIGHT))

for i in range(length):
	image = Image.open('image/normal/%d-%d.png' % nums[i])
	photo = ImageTk.PhotoImage(image)
	photos[i] = photo

	l = tkinter.Label(image = photo)
	l.pack()
	l.place(x = IMAGE_WIDTH * i, y = 0, width = IMAGE_WIDTH, height = IMAGE_HEIGHT)

root.mainloop()
