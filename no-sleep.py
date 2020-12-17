import time
import pyautogui
import random

# sudo apt-get install scrot

def gen_random():
	return random.randint(200,300)
old_x , old_y = pyautogui.position()
pyautogui.FAILSAFE = False
print("Ok")

while 1:
	#sleep for 5*60 => 5mins	
	time.sleep(120)
	
	c_x , c_y = pyautogui.position()
	x , y = gen_random() ,gen_random()

	if old_x == c_x and old_y == c_y:
		pyautogui.moveTo(x,y,duration=0.10)

	old_x, old_y = c_x , c_y
	
