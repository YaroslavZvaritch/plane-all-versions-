import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Мое первое приложение на Tkinter")  # Устанавливаем заголовок окна
root.geometry("400x300")  # Устанавливаем размеры окна (ширина x высота)
root.resizable(True, True)
root.minsize(1,1)
root.maxsize(1920,1080)
root.iconbitmap(default="controller.ico")
A = 0
B = 0
def soobshenie(vivodimoe_na_ecran):
    global A,B
    G = True
    if vivodimoe_na_ecran.widget["text"] == "":
        if A % 2 == 0:
            vivodimoe_na_ecran.widget["text"] = "X"
            G = True
        else:
            vivodimoe_na_ecran.widget["text"] = "O"
            G = False
        A += 1
        B += 1
        if B % 9 == 0:
            otchistka(A)
        proverkanapobedy1(G)
def pobeda(G):
    otchistka(A)
def proverkanapobedy1(E):
    global h
    T = ""
    if (h[0]["text"] == "X"  and h[4]["text"] == "X" and h[8]["text"] == "X") or (h[0]["text"] == "O"  and h[4]["text"] == "O" and h[8]["text"] == "O"):
        print("Победили игрок который играл за " + h[0]["text"])
        messagebox.showinfo("pobeda","Победили игрок который играл за " + h[0]["text"])
        pobeda(E)
    if (h[0]["text"] == "X" and h[4]["text"] == "X" and h[6]["text"] == "X") or (h[2]["text"] == "O" and h[4]["text"] == "O" and h[6]["text"] == "O"):
        print("Победили игрок который играл за " + h[2]["text"])
        pobeda(E)
    for i in range(3):
        if (h[i * 3]["text"] == "X" and h[i * 3 + 1]["text"] == "X" and h[i * 3 + 2]["text"] == "X") or (h[i]["text"] == "X" and h[i + 3]["text"] == "X" and h[i + 6]["text"] == "X"):
            pobeda(h)
            if E == True:
                T = "X"
            else:
                T = "O"
            print("Победили игрок который играл за " + T)
        if (h[i * 3]["text"] == "O" and h[i * 3 + 1]["text"] == "O" and h[i * 3 + 2]["text"] == "O") or (h[i]["text"] == "O" and h[i + 3]["text"] == "O" and h[i + 6]["text"] == "O"):
            pobeda(h)
            if E == True:
                T = "X"
            else:
                T = "O"
            print("Победили игрок который играл за " + T)
def otchistka(ratatyi):
    global h
    for d in h:
        d["text"] = ""
button2 = tk.Button(root, text="clear")
button2.bind("<ButtonPress-1>", otchistka)
h = []
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="",height=2,width=2,padx=100,pady=100,font=["Arial",10])
        button.grid(row=i,column=j)
        h.append(button)
        button.bind("<ButtonPress-1>",soobshenie)
button2.grid(row=3,column=1)
root.mainloop()