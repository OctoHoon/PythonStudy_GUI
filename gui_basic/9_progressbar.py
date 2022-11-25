import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480") # 가로 * 세로 + X좌표 + Y좌표

# progressbar = ttk.Progressbar(root, maximum = 100, mode="indeterminate") # mode: indeterminate(언제 끝날지 모르는 경우)
# progressbar = ttk.Progressbar(root, maximum = 100, mode="determinate") # mode: determinate(언제 끝날지 아는 경우)
# progressbar.start(10) # 10 ms 마다 움직임, progressbar 실행
# progressbar.pack()


# def btncmd():
#    progressbar.stop() # 작동 중지
#
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
   for i in range(1, 101):
      time.sleep(0.01) # 0.01초 대기

      p_var2.set(i) # progress bar 의 값 설정
      progressbar2.update() # ui 업데이트
      print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()