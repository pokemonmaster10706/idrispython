import pyautogui , time

content = input("enter content: ")
contenta = input('enter content: ')

t = int(input('enter wait time: '))

time.sleep(t)

pyautogui.typewrite(content)
pyautogui.typewrite(contenta)
