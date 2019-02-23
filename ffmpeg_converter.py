#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:01:26 2019

@author: Johnny Rong

"""

import subprocess
import os
import sys
import termios
import time
import tkinter as tk
from tkinter import filedialog

version = "1.0" #版本号
ffmpeg_path = "~/ffmpeg/" # 默认 ffmpeg 存放路径
output_path = "~/Downloads/ffmpeg_output/" # 文件输出路径

def welcome(): # 欢迎界面
	print ("")
	print ("")
	print ("############################")
	print ("##                        ##")
	print ("##  Video Converter v%s  ##" %(version))
	print ("##                        ##")
	print ("############################")
	print ("")
def press_any_key_exit(msg): # 
  # 获取标准输入的描述符
  fd = sys.stdin.fileno()

  # 获取标准输入(终端)的设置
  old_ttyinfo = termios.tcgetattr(fd)

  # 配置终端
  new_ttyinfo = old_ttyinfo[:]

  # 使用非规范模式(索引3是c_lflag 也就是本地模式)
  new_ttyinfo[3] &= ~termios.ICANON
  # 关闭回显(输入不会被显示)
  new_ttyinfo[3] &= ~termios.ECHO

  # 输出信息
  sys.stdout.write(msg)
  sys.stdout.flush()
  # 使设置生效
  termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
  # 从终端读取
  os.read(fd, 7)

  # 还原终端设置
  termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)
def select():			# 源文件选择
    print ("Please select the origin video file: ")
    press_any_key_exit("Press any key to continue...")
 
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    print ("Source File: " + path)
    #print (origin_path)
    return path
def v_encoder():		# 视频编码器设置
	print ("")
	print ("Please choose the encoder:")
	print ("1. libx264 2.libx265")
	encoder_id = input("[1/2]? ")

	if encoder_id == "2":
		encoder_str = "libx265"
	else:
		encoder_str = "libx264"
	print("Video encoder set to '" + encoder_str +"'.")
	return encoder_str #	
def output():			# 封装格式设置
	print ("")
	format_str = input("Please input the format. Such as 'mp4' or 'avi' " )
	return format_str		
def speed():			# 编码速度设置
	print ("")
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
def tune():				# 编码优化设置(未使用)
	print ("Please choose the tune: ")
	print ("1. Flim 2. Animation 3. Grain 4. Fastdecode 5. Zerolatency")
	tune_id = input("[1~5]? ")

	if tune_id == "2":
		tune_str = "animation"
	elif tune_id == "3":
		tune_str = "grain"
	elif tune_id == "4":
		tune_str = "fastdecode"
	elif tune_id == "5":
		tune_str = "zerolatency"
	else:
		tune_str = "flim"

	return tune_str			
def filename():			# 输出文件名设置
	filename_str = input ("Please input the output filename: ")
	return filename_str		
def command():			# 指令生成
	file_origin = select()
	time.sleep(0.5)
	info = ffmpeg_path + "ffmpeg -i " + file_origin
	subprocess.call(info, shell=True)
	print ("")
	print ("Do you want to convert the file?")
	convert_confirm = input ("Contiune? [Y/N] ")
	if convert_confirm == "y":
		time.sleep(0.5)
	else:
		sys.exit()

	v_encoder_str = "libx264" 	# 默认视频编码器
	format_str = "mp4"			# 默认封装格式
	speed_str = "ultrafast"		# 默认编码速度

	parameter_id = "0"
	while parameter_id != "4":
		print ("")
		print ("Please choose the parameter.")
		print ("1. Video encoder (Default: libx264)") 	
		print ("2. Format (Default: mp4)")				
		print ("3. Convert speed (Default: ultrafast)") 
		print ("4. Done")
		parameter_id = input("[1~4]? ")
		if parameter_id == "1":
			v_encoder_str = v_encoder()
		elif parameter_id == "2": 
			format_str = output()
		elif parameter_id == "3":
			speed_str = speed()
	
	time.sleep(0.5)
	print ("")
	filename_str = filename()

	# 确认设置
	time.sleep(0.5)
	print ("")
	print ("Confirmation:")
	print ("You will convert 'file_origin' to format '" + format_str + "' with encoder '" + v_encoder_str + "'and convert speed '" + speed_str + "'.")
	confirm = input ("Contiune? [Y/N] ")
	if confirm == "y":
		time.sleep(0.5)
	else:
		sys.exit()

	# 生成指令
	command_str = ffmpeg_path + "ffmpeg -i " + file_origin + " -c:v " + v_encoder_str + " -c:a copy -preset " + speed_str + " " + output_path + filename_str + "." + format_str

	return command_str 		  		

welcome()
str = command()
#print (str)
subprocess.call(str, shell=True)

press_any_key_exit("Press any key to exit...")
sys.exit() #程序退出