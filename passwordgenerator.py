from tkinter import *
import random

window=Tk()
window.title('Password Generator')
window.geometry('500x300')


label1 = Label(window,text='Password Generator',width=25,height=2,font='Ivy 20 bold')
label1.place(x=15,y=2)

label2 = Label(window, text='Enter user name:',width=20,height=1,font='Ivy 12')
label2.place(x=15,y=80)

label3 = Label(window, text='Enter password length:',width=20,height=1,font='Ivy 12')
label3.place(x=15, y=120)

label4 = Label(window, text='Generated password:',width=20,height=1,font='Ivy 12')
label4.place(x=15, y=200)

entry1 = Entry(window, width=30, font='Ivy 12')
entry1.place(x=200, y=80)

entry2 = Entry(window, width=30, font='Ivy 12')
entry2.place(x=200, y=120)

entry3 = Entry(window, width=30, font='Ivy 12')
entry3.place(x=200, y=200)

def generate():

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbol = "(){}[].,@#$^&*_;/!"
    num = "0123456789"

    all = lower + upper + symbol + num

    n = int(entry2.get())

    password = "".join(random.sample(all, n))

    entry3.delete(0, END)
    entry3.insert(0, password)


b = Button(window,width=15,height=1,text='Generate Password',command=generate)
b.place(x=170, y=160)


window.mainloop()