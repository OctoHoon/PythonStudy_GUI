from tkinter import *

root = Tk()
root.title("Hoon GUI")
root.geometry("640x480") # 가로 * 세로 + X좌표 + Y좌표

txt = Text(root, width=30, height=5) # 여러 줄에 걸쳐 써야 할 때
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 한 줄만 필요할때. 예시) 아이디, 패스워드
e.pack()

e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1번째 라인, 0번째 column 부터 END 끝까지 가져오기
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()



root.mainloop()