#!/usr/bin/env python3

# Copyright 2016 Sugizaki Yukimasa
# This software is licensed under CC BY-SA 4.0.

import sys
import tkinter
from PIL import Image, ImageTk

IMAGE_WIDTH = 64
IMAGE_HEIGHT = 102

photos_normal = [None for i in range(12 * 4)]
photos_darken = [None for i in range(12 * 4)]
ls = [None for i in range(12 * 4)]
selected = [False for i in range(12 * 4)]

def print_and_exit_program(x):
	is_first = True
	for i in range(12):
		for j in range(4):
			if selected[i * 4 + j]:
				if not is_first:
					print(" ", end = "")
				else:
					is_first = False
				print(i * 4 + j, end = "")

	# If printed
	if not is_first:
		print()

	exit(0)

def mouse_clicked(event):
	i = int((event.x_root - root.winfo_rootx()) / IMAGE_WIDTH)
	j = int((event.y_root - root.winfo_rooty()) / IMAGE_HEIGHT)

	flag = False
	if not (0 <= i < 12):
		print("i out-of-range: %d" % (i))
		flag = True
	if not (0 <= j < 4):
		print("j out-of-range: %d" % (j))
		flag = True
	if flag:
		return

	if selected[i * 4 + j]:
		#print("Deselected (%d, %d)" % (i, j))
		ls[i * 4 + j].configure(image = photos_normal[i * 4 + j])
		selected[i * 4 + j] = False
	else:
		#print("Selected (%d, %d)" % (i, j))
		ls[i * 4 + j].configure(image = photos_darken[i * 4 + j])
		selected[i * 4 + j] = True

root = tkinter.Tk()
root.bind("<KeyPress-q>", print_and_exit_program)
root.geometry('%dx%d' % (IMAGE_WIDTH * 12, IMAGE_HEIGHT * 4))

for i in range(12):
	for j in range(4):
		image = Image.open('image/normal/%d-%d.png' % (i + 1, j + 1))
		photo_normal = ImageTk.PhotoImage(image)

		image = Image.open('image/dark/%d-%d.png' % (i + 1, j + 1))
		photo_darken = ImageTk.PhotoImage(image)

		l = tkinter.Label(image = photo_normal)
		l.bind("<Button-1>", mouse_clicked)
		l.pack()
		l.place(x = IMAGE_WIDTH * i, y = IMAGE_HEIGHT * j, width = IMAGE_WIDTH, height = IMAGE_HEIGHT)

		photos_normal[i * 4 + j] = photo_normal
		photos_darken[i * 4 + j] = photo_darken
		ls[i * 4 + j] = l

root.mainloop()
