import pyautogui , time
time.sleep(5)
f = open("weather.txt" , "r")
t = open("silentvoice.txt" , "r")
pyautogui.typewrite('script of a silent voice')
pyautogui.press('enter')
for word in t:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(10)
pyautogui.typewrite('script of weathering with you')
pyautogui.press('enter')
for l in f:
    pyautogui.typewrite(l)
    pyautogui.press("enter")
    time.sleep(10)
