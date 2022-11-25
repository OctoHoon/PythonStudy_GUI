from tkinter import *

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="C:/Users/Admin/PycharmProjects/pythonProject2/gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요")

    global photo2 # 함수가 끝나도 garbage collector가 photo2 변수를 지우지 않도록 전역변수로 설정
    photo2 = PhotoImage(file="C:/Users/Admin/PycharmProjects/pythonProject2/gui_basic/img2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()