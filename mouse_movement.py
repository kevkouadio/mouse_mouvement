import pyautogui
import random
import time

while True:
    # Get the screen's width and height
    screen_width, screen_height = pyautogui.size()

    # Calculate random coordinates within the screen
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Move the mouse to the random coordinates
    pyautogui.moveTo(x, y)

    # Pause for 10 seconds
    time.sleep(15)
