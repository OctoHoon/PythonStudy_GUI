from tkinter import *

root = Tk()
root.title("Hoon GUI")
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+300+100") # 가로 * 세로 + X좌표 + Y좌표

root.resizable(False, False) # 창 크기 (x,y) 값 변경 불가


root.mainloop()