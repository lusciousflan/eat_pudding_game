#coding:utf-8

import tkinter as tk

root = tk.Tk() #ウィンドウ作成
root.geometry("400x600") #ウィンドウサイズ変更
root.title("pudding!") #ウィンドウ名変更
root.configure(bg="#FFE47C") #ウィンドウの背景色 #RRGGBB

frame1 = tk.Frame(
    root,
    background = "#FFE47C",
    width = 400,
    height = 600,
    )
frame1.pack() #インスタンスを配置

label1 = tk.Label(
    root,
    text="ぷりんをひたすら食べるだけ",
    font=("コーポレート・ロゴ Bold", 20),
    fg="#663800",
    bg="#FFE47C"
    ) #text表示 fg文字色、bg背景色
label1.place(x = 30, y = 20) #text位置変更

button1 = tk.Button(
    root,
    text = "すたぁと",
    font=("コーポレート・ロゴ Bold", 20)
    ) #ボタン作成
button1.place(x = 140,y = 500) #ボタン位置変更

root.mainloop() #ウィンドウ表示
