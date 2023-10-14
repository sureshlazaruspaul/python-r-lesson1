# Move cursor and play an audio file

"""
Move the cursor to the specified coordinates (x, y) with 
a specified move duration, then simulate a mouse click at 
those coordinates with a specified click duration.

parameters:
x: X-coordinate on the screen
y: Y-coordinate on the screen
click_duration: Duration of the mouse click simulation 
(default is 1.5 seconds)
move_duration: Duration of the cursor movement 
(default is 2 seconds)

requirements:
- pip install pyautogui
"""

import pyautogui
import time

def move_and_play(x, y, click_duration=1.5, move_duration=2):
    pyautogui.moveTo(x, y, duration=move_duration)
    time.sleep(2)
    pyautogui.click(x, y, duration=click_duration)

# USAGE
# move_and_play(100, 480)
# move_and_play(300, 480)
# move_and_play(1025, 450)