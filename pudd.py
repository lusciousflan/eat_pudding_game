#coding:utf-8
#Frameをクラス化しない

import tkinter as tk
import tkinter.messagebox as messa
import random

def eatpudding():
    global score, puddingPlace, ScoreLabel
    if(puddingPlace[13][mikotoPlace] == 1):
        score = score + 1
        ScoreLabel.set("Score: " + str(score))
        puddingPlace[13][mikotoPlace] = 0
    canvas1.after(100,eatpudding)

def puddingMove():
    global puddingPlace
    for i in range(10):
        if(puddingPlace[13][i] == 1):
            canvas1.create_rectangle(i*40, 520, (i+1)*40, 560, fill="#FFE47C", width=0)
            puddingPlace[13][i] = 0
    for i in range(13):
        for j in range(10):
            if(puddingPlace[12-i][j] == 1):
                puddingPlace[12-i][j] = 0
                puddingPlace[13-i][j] = 1
                canvas1.create_rectangle(j*40, (12-i)*40, (j+1)*40, (13-i)*40, fill="#FFE47C", width=0)
                canvas1.create_image(40*j, (13-i)*40, image = pudding, anchor = tk.NW)
    rp = random.randint(0,9)
    puddingPlace[0][rp] = 1
    canvas1.create_image(40*rp, 0, image = pudding, anchor = tk.NW)
    canvas1.after(700,puddingMove)

def mikotoMoveR(event):
    global mikotoPlace
    if(mikotoPlace < 9):
        mikotoPlace = mikotoPlace + 1
        canvas1.create_image(40 * mikotoPlace, 520, image = mikoto, anchor = tk.NW)
        canvas1.create_rectangle((mikotoPlace-1)*40, 520, mikotoPlace*40, 560, fill="#FFE47C", width = 0)

def mikotoMoveL(event):
    global mikotoPlace
    if(mikotoPlace > 0):
        mikotoPlace = mikotoPlace - 1
        canvas1.create_image(40 * mikotoPlace, 520, image = mikoto, anchor = tk.NW)
        canvas1.create_rectangle((mikotoPlace+1)*40, 520, (mikotoPlace+2)*40, 560, fill="#FFE47C", width = 0)

def ChangePage(page):
    page.tkraise()

def GameStart():
    canvas1.create_image(0, 520, image = mikoto, anchor = tk.NW)

def ButtonStart():
    ChangePage(frame2)
    GameStart()

if(__name__ == "__main__"):
    root = tk.Tk()
    root.geometry("400x600")
    root.title("pudding!")
    pudding = tk.PhotoImage(file="pudding.png")
    spoon = tk.PhotoImage(file="spoon.png")
    mikoto = tk.PhotoImage(file="mikoto.png")
    
    #frame2
    score = 0
    ScoreLabel = tk.StringVar()
    ScoreLabel.set("Score: " + str(score))
    frame2 = tk.Frame(
        root,
        bg = "#FFE47C",
        width = 400,
        height = 600,
        )
    frame2.place(x = 0, y = 0)
    canvas1 = tk.Canvas(
        frame2,
        width = 400,
        height = 560,
        bg = "#FFE47C",
        )
    canvas1.place(x = 0, y = 0)

    #frame2の処理
    mikotoPlace = 0
    canvas1.bind("<Button-3>", mikotoMoveR)
    canvas1.bind("<Button-1>", mikotoMoveL)
    puddingPlace = [[0 for i in range(10)] for j in range(14)]
    puddingMove()


    LabelScore = tk.Label(
        frame2,
        textvariable = ScoreLabel,
        font = ("コーポレート・ロゴ Bold", 18),
        fg = "#663800",
        bg = "#FFE47C",
        )
    LabelScore.place(x = 0, y = 570)
    eatpudding()
    
    #frame1
    frame1 = tk.Frame(
        root,
        bg = "#FFE47C",
        width = 400,
        height = 600,
        )
    frame1.place(x = 0, y = 0)
    LabelTitle = tk.Label(
        frame1,
        text="ぷりんをひたすら食べるだけ",
        font=("コーポレート・ロゴ Bold", 20),
        fg = "#663800",
        bg = "#FFE47C",
        )
    LabelTitle.place(x = 30, y = 20)
    button1 = tk.Button(
        frame1,
        text = "すたぁと",
        font=("コーポレート・ロゴ Bold", 20),
        command = ButtonStart,
        )
    button1.place(x = 140, y = 500)

    root.mainloop()
    
