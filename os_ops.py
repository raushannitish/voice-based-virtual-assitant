import os
import subprocess as sp
import datetime
import random
import cv2
import pyautogui #functions for automating mouse and keyboard actions on the screen.
import time
def open_notepad():
    os.startfile('notepad.exe')

def open_cmd():
    os.system('start cmd')

def open_camera():
    print("Opening Camera")
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        elif k == ord('s'): # press 's' to take a picture
            img_name = "opencv_frame.png"
            cv2.imwrite(img_name, img)
            print(f"{img_name} saved successfully!")
            break

    cap.release()
    cv2.destroyAllWindows()

def open_calculator():
    sp.Popen('calc.exe')
def tellDay():
	day = datetime.datetime.today().weekday() + 1
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		return day_of_the_week
def tellTime():
	time = str(datetime.datetime.now())
	print(time)
	hour = time[11:13]
	min = time[14:16]
	return hour,min
def play_music():
    music_dir = 'D:\\Music' #Add your music directory path here
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, random.choice(songs)))
    
def stop_music():
    print("Stopping music")
    os.system("taskkill /f /im Music.UI.exe")
    
def take_screenshot():
    print("Taking screenshot")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save("screenshot.png")


def shutdown():
    os.system('shutdown /s /t 0')