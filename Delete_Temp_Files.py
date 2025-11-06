import pyautogui
import time
import os

# Optional: make automation slower & safer
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True  # move mouse to top-left corner to stop

# Step 1: Open Run dialog (Win + R)
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Step 2: Type %temp% and press Enter
pyautogui.typewrite('%temp%\n', interval=0.1)
time.sleep(2)  # wait for File Explorer to open

# Step 3: Select all files (Ctrl + A)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)

# Step 4: Press Delete
pyautogui.press('delete')
time.sleep(2)

# Step 5: Confirm delete (press Enter if confirmation window appears)
pyautogui.press('enter')

# Optional: close File Explorer
time.sleep(3)
pyautogui.hotkey('alt', 'f4')

print("✅ Temp files cleanup automated successfully!")

# Step 6: Repeat for system temp
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite('temp\n', interval=0.1)
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.press('delete')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('alt', 'f4')

