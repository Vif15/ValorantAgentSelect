import random
import time
import pyautogui as gui
import csv

import userPath

# gui.moveTo(100, 100, duration = 0)
# gui.click(143, 246)


with open(userPath.path, 'r') as file:
    reader = csv.reader(file)
    data_list = list(reader)

c = 0
num = random.choice(list(range(2, 25)))
for agent in data_list:
    c += 1
    if c == num:
        gui.move(int(agent[0]), int(agent[1]))
        time.sleep(0.2)
        gui.click(int(agent[0]), int(agent[1]))
        time.sleep(0.2)
        gui.click(int(agent[0]), int(agent[1]))
        time.sleep(0.2)
        gui.click(int(agent[0]), int(agent[1]))
        time.sleep(0.2)
        print(agent[2])
        time.sleep(1)
gui.move(945, 760)
time.sleep(1)
gui.click(945, 760)
# while True:
#     time.sleep(1.5)
#     print(gui.position())
