import pyautogui
import os
import time
import schedule

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def imageClick(pos):
    i = pyautogui.center(pos)
    print(i)
    pyautogui.click(i[0], i[1])

def repeat():
    # 실제 작동시킬 코드
    try:
        imageClick(pyautogui.locateOnScreen("1chatting.png"))
        time.sleep(1)
        imageClick(pyautogui.locateOnScreen("2grouptalk.png"))
        time.sleep(1)
        imageClick(pyautogui.locateOnScreen("3shareYellow.png"))
        time.sleep(3)
        imageClick(pyautogui.locateOnScreen("4close.png"))
    except:
        print("except")
        pass

    # try:
    #     imageClick(pyautogui.locateOnScreen("testMy.png"))
    #     print("testMy")
    #     time.sleep(1)
    #     imageClick(pyautogui.locateOnScreen("3shareYellow.png"))
    #     print("share")
    #     time.sleep(3)
    #     imageClick(pyautogui.locateOnScreen("4close.png"))
    #     print("close")
    # except:
    #     print("except")
    #     pass


schedule.every(30).seconds.do(repeat)

while True:
    schedule.run_pending()
    time.sleep(1)