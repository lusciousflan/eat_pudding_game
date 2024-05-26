#coding:utf-8
#Frameをクラス化しない

import tkinter as tk
import tkinter.messagebox as messa
import random

def ChangePage(page):
    page.tkraise()

def GameOver():
    global score, gaming, puddingPlace, timering
    for i in range(10):
        for j in range(14):
            puddingPlace[j][i] = 0
    canvas1.create_rectangle(0, 0, 400, 560, fill="#FFE47C", width=0)
    gaming = 1
    timering = 1
    ChangePage(frame3)
    yourscore = tk.Label(
        frame3,
        text = "あなたのスコア: " + str(score) + "  ",
        font = ("コーポレート・ロゴ Bold", 20),
        fg = "#663800",
        bg = "#FFE47C",
        )
    yourscore.place(x = 90, y = 120)

def eatpudding():
    global score, puddingPlace, ScoreLabel, life
    if(puddingPlace[13][mikotoPlace] == 1):
        score = score + 1
        ScoreLabel.set("Score: " + str(score))
    elif(puddingPlace[13][mikotoPlace] == 2):
        life = life - 1
        LifeLabel.set("Life: " + str(life))
        if(life == 0):
            GameOver()
    puddingPlace[13][mikotoPlace] = 0
    canvas1.after(200,eatpudding)

def puddingMove():
    global puddingPlace, gaming
    for i in range(10):
        if(puddingPlace[13][i] == 1 or puddingPlace[13][i] == 2):
            canvas1.create_rectangle(i*40, 520, (i+1)*40, 560, fill="#FFE47C", width=0)
            puddingPlace[13][i] = 0
    for i in range(13):
        for j in range(10):
            if(puddingPlace[12-i][j] == 1):
                puddingPlace[12-i][j] = 0
                puddingPlace[13-i][j] = 1
                canvas1.create_rectangle(j*40, (12-i)*40, (j+1)*40, (13-i)*40, fill="#FFE47C", width=0)
                canvas1.create_image(40*j, (13-i)*40, image = pudding, anchor = tk.NW)
            elif(puddingPlace[12-i][j] == 2):
                puddingPlace[12-i][j] = 0
                puddingPlace[13-i][j] = 2
                canvas1.create_rectangle(j*40, (12-i)*40, (j+1)*40, (13-i)*40, fill="#FFE47C", width=0)
                canvas1.create_image(40*j, (13-i)*40, image = spoon, anchor = tk.NW)
    rp = random.randint(0,9)
    sorp = random.randint(0,3)
    if(sorp == 0):
        puddingPlace[0][rp] = 1
        canvas1.create_image(40*rp, 0, image = pudding, anchor = tk.NW)
    else:
        puddingPlace[0][rp] = 2
        canvas1.create_image(40*rp, 0, image = spoon, anchor = tk.NW)
    if(gaming == 0):
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

def Timer():
    global countdown, nowTime, timering
    countdown = countdown - 1
    nowTime.set(str(countdown))
    if(countdown == 0):
        GameOver()
    if(timering == 0):
        frame2.after(1000, Timer)

def GameStart():
    canvas1.create_image(0, 520, image = mikoto, anchor = tk.NW)
    global score, mikotoPlace, life, countdown, timering
    mikotoPlace = 0
    score = 0
    countdown = 41
    timering = 0
    ScoreLabel.set("Score: " + str(score))
    LifeLabel.set("Life: " + str(life))
    puddingMove()
    eatpudding()
    Timer()

def ButtonStart():
    global gaming
    gaming = 0
    ChangePage(frame2)
    GameStart()

def ButtonEnd():
    global score, life
    score = 0
    life = 3
    ChangePage(frame1)

if(__name__ == "__main__"):
    root = tk.Tk()
    root.geometry("400x600")
    root.title("pudding!")
    pudding = tk.PhotoImage(file="pudding.png")
    spoon = tk.PhotoImage(file="spoon.png")
    mikoto = tk.PhotoImage(file="mikoto2.png")
    #frame3
    score = 0
    frame3 = tk.Frame(
        root,
        bg = "#FFE47C",
        width = 400,
        height = 600,
        )
    frame3.place(x = 0, y = 0)
    gameover = tk.Label(
        frame3,
        text = "ゲームオーバー",
        font = ("コーポレート・ロゴ Bold", 20),
        fg = "#663800",
        bg = "#FFE47C",
        )
    gameover.place(x = 100, y = 50)
    GoStart = tk.Button(
        frame3,
        text = "タイトルへ戻る",
        font=("コーポレート・ロゴ Bold", 20),
        command = ButtonEnd,
        )
    GoStart.place(x = 100, y = 500)
    
    #frame2
    countdown = 41
    timering = 1
    ScoreLabel = tk.StringVar()
    ScoreLabel.set("Score: " + str(score))
    life = 3
    LifeLabel = tk.StringVar()
    LifeLabel.set("Life: " + str(life))
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
    LabelLife = tk.Label(
        frame2,
        textvariable = LifeLabel,
        font = ("コーポレート・ロゴ Bold", 18),
        fg = "#663800",
        bg = "#FFE47C",
        )
    LabelLife.place(x = 300, y = 570)
    nowTime = tk.StringVar()
    nowTime.set(str(countdown))
    nowTimeLabel = tk.Label(
        frame2,
        textvariable = nowTime,
        font = ("コーポレート・ロゴ Bold", 18),
        bg = "#FFE47C",
        fg = "#663800",
        )
    nowTimeLabel.place(x = 180, y = 570)

    #frame2の処理
    mikotoPlace = 0
    gaming = 0
    canvas1.bind("<Button-3>", mikotoMoveR)
    canvas1.bind("<Button-1>", mikotoMoveL)
    puddingPlace = [[0 for i in range(10)] for j in range(14)]


    LabelScore = tk.Label(
        frame2,
        textvariable = ScoreLabel,
        font = ("コーポレート・ロゴ Bold", 18),
        fg = "#663800",
        bg = "#FFE47C",
        )
    LabelScore.place(x = 0, y = 570)
    
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
    
