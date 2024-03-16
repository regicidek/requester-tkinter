from tkinter import *
from webbrowser import *

def yt():
    yts = ent.get()
    open(f'https://www.youtube.com/results?search_query={yts}')

def gl():
    gls = enta.get()
    open(f'https://www.google.ru/search?q={gls}')

def wp():
    wps = entb.get()
    open(f'https://ru.wikipedia.org/wiki/{wps}')

w = Tk()
w.geometry('500x500')
w.config(bg='darkgreen')
lbl = Label(w,text="enter a request (youtube)",bg='darkgreen')
ent = Entry(w, bg='green')
btn = Button(w,text="start",bg='green', command=yt)
lbl.pack()
ent.pack()
btn.pack()
lbla = Label(w,text="enter a request (google)",bg='darkgreen')
enta = Entry(w, bg='green')
btna = Button(w,text="start",bg='green', command=gl)
lbla.pack()
enta.pack()
btna.pack()
lblb = Label(w,text="enter a request (wikipedia)",bg='darkgreen')
entb = Entry(w, bg='green')
btnb = Button(w,text="start",bg='green', command=wp)
lblb.pack()
entb.pack()
btnb.pack()




mainloop()