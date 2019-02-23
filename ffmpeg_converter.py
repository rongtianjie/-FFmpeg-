#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:01:26 2019

@author: Johnny Rong
"""

import subprocess
import os
import time
import tkinter as tk
from tkinter import filedialog

def select():
    print ("Please select the origin video file: ")
    time.sleep(1)
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    print ("Source File: " + path)
    #print (origin_path)
    return path
def encoder():
	print ("Please choose the encoder:")
	encoder_id = input("1. libx264 2.libx265 [1/2]? ")

	if encoder_id == "2":
		encoder_str = "libx265"
	else:
		encoder_str = "libx264"
	print("Video encoder set to '" + encoder_str +"'.")
	return encoder_str
def output():
	format_str = input("Please input the format. Such as 'mp4' or 'avi' " )
	return format_str
def speed():
	print ("Please choose the encode speed: ")
	print ("1. Ultrafast 2. Veryfast 3. Medium 4. Slower 5. Placebo")
	speed_id = input("[1~5]? ")

	if speed_id == "1":
		speed_str = "ultrafast"
	elif speed_id == "2":
		speed_str = "veryfast"
	elif speed_id == "4":
		speed_str = "slower"
	elif speed_id == "5":
		speed_str = "Placebo"
	else:
		speed_str = "medium"
	print("Convert speed set to '" + speed_str +"'.")
	return speed_str
def tune():
	print ("Please choose the tune: ")
	print ("1. Flim 2. Animation 3. Grain 4. Fastdecode 5. Zerolatency")
	tune_id = input("[1~5]? ")

	if tune_id == 2:
		tune_str = "animation"
	elif tune_id == 3:
		tune_str = "grain"
	elif tune_id == 4:
		tune_str = "fastdecode"
	elif tune_id == 5:
		tune_str = "zerolatency"
	else:
		tune_str = "flim"

	return tune_str
def filename():
	filename_str = input ("Please input the output filename: ")
	return filename_str
def command():
	file_origin = select()
	encoder_str = encoder()
	format_str = output()
	speed_str = speed()
	#tune_str = tune()
	filename_str = filename()
	time.sleep(1)
	print ("Confirmation:")
	print ("You will convert the file to format '" + format_str + "' with encoder '" + encoder_str + "'and convert speed '" + speed_str + "'.")
	confirm = input ("Contiune? [Y/N] ")
	if confirm == "y":
		time.sleep(0.5)
	else:
		os.system("pause")

	command_str = "~/ffmpeg/ffmpeg -i " + file_origin + " -c:v " + encoder_str + " -c:a copy -preset " + speed_str + " ~/Downloads/ffmpeg_output/" + filename_str + "." + format_str

	return command_str

str = command()
#print (str)
subprocess.call(str, shell=True)