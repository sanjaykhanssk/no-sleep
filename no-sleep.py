import time
import pyautogui
import random

# sudo apt-get install scrot

def gen_random():
	return random.randint(200,300)
old_x , old_y = pyautogui.position()

print("Ok, I'm Awake")

while 1:
	#sleep for 5*60 => 5mins	
	time.sleep(1)
	
	c_x , c_y = pyautogui.position()

	if (old_x,old_y) == (c_x,c_y):
		x , y = gen_random() ,gen_random()
		pyautogui.moveTo(x,y,duration=0.10)
		print(True)
	old_x, old_y = x, y
	
