#coding:utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg

def ChangePage(page):#frameを二枚重ねにしておいて上下を入れ替える
    page.tkraise()

def ButtonStart():
    ChangePage(f2)

class Frame1(tk.Frame): #フレームをクラス化 Frame1はスタート画面
    def __init__(self, master=None): #コンストラクタ
        super().__init__(master, width=400, height=600) #tk.Frameの機能をmasterで呼び出す？

        self.master.title("pudding!")

        self.config(bg="#FFE47C")
        self.propagate(False)

        self.place(x = 0, y = 0)
        self.create_widget()

    def create_widget(self):

        self.label1 = tk.Label(
            self,
            text="ぷりんをひたすら食べるだけ",
            font=("コーポレート・ロゴ Bold", 20),
            fg = "#663800",
            bg = "#FFE47C"
            )
        self.label1.place(x = 30, y = 20)

        self.button1 = tk.Button(
            self,
            text = "すたぁと",
            font=("", 20),
            command = ButtonStart,
            )
        self.button1.place(x = 140, y = 500)

class Frame2(tk.Frame): #Frame2はゲーム画面
    def __init__(self,master=None):
        super().__init__(master, width=400, height=600)

        self.config(bg = "#FFE47C")
        self.propagate(False)

        self.place(x=0,y=0)
        self.create_widget()

    def create_widget(self):
        self.score = tk.Label(
            self,
            text = "Score:",
            font = ("コーポレート・ロゴ Bold", 18),
            fg = "#663800",
            bg = "#FFE47C"
            )
        self.score.place(x = 0,y = 570)
        canvas1.create_image(0, 0, image = pudding, anchor = tk.NW)
        

if(__name__ == "__main__"):
    root = tk.Tk()
    root.geometry("400x600")
    pudding = tk.PhotoImage(file="pudding.png")
    spoon = tk.PhotoImage(file="spoon.png")
    canvas1 = tk.Canvas(
        root,
        width = 400,
        height = 570,
        bg = "#FFE47C",
        )
    canvas1.place(x = 0, y = 0)
    f2 = Frame2(master=root)
    f1 = Frame1(master=root)
    root.mainloop()
