import webbrowser
import time
import pyautogui

# Step 1: Open Google in the default browser
webbrowser.open("https://www.google.com")
time.sleep(5)  # wait for browser to open

# Step 2: Click on the search bar (adjust x,y based on your screen)
pyautogui.click(859, 529)   # Example position, change as per your screen
time.sleep(1)

# Step 3: Type the search query
pyautogui.write("South Africa vs Australia score", interval=0.05)
pyautogui.press("enter")
time.sleep(5)  # wait for results to load

# Step 4: Click on the first link (adjust x,y to your screen)
pyautogui.click(391, 432)   # Example position, change as per your screens
