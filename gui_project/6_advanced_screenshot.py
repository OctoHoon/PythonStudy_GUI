import keyboard
from PIL import ImageGrab
import time


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot) # F9 외에 다른 키도 가능. ctr1+shift+s, a 등등

keyboard.wait("esc") # 사용자가 esc 누를 때 까지 프로그램 수행