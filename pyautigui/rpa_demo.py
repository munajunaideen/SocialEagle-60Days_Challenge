import pyautogui
import time #for time setum --Sleep --wait

#Mouse Operation 
'''
pyautogui.click(1227,290)
time.sleep(2)
pyautogui.rightClick(100,100)

x,y = pyautogui.position()
print(f'x: {x}, y: {y}')

pyautogui.doubleClick(100,100)

pyautogui.drag(100,100, 200,200)
pyautogui.scroll(-500)
'''

#Keyboard Operation
'''
time.sleep(5)

pyautogui.click(406,675)

time.sleep(1)
pyautogui.write('Socialeagle.ai')

pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
'''


#Image
"""location = pyautogui.locateOnScreen('shot21.png', confidence=0.8)

print(location)

time.sleep(3)
pyautogui.click(pyautogui.center(location))"""

#to screenshot

"""ss = pyautogui.screenshot()
ss.save('ss.png')"""

#size = pyautoguSocialeagle.ai
# i.size()
#print(size)

#print(pyautogui.size())