import pyautogui
import random

pyautogui.click(1500, 1150, 1, 0, 'left')
for i in range(20):
  if random.randint(1,6) != 6:
    pyautogui.typewrite('I love you\n')
  else:
    pyautogui.typewrite('Fuck you\n')
