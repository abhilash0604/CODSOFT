from tkinter import *
from tkinter import messagebox as mb
import requests
from datetime import datetime

window=Tk()
window.title('Weather Application')
window.geometry('800x500')
window.configure(bg='sky blue')

def get_weather():
    global city
    city=entry1.get()
    api_key='110fa0a8c65a12e069fab440aee2bb6c'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        temp=data['main']['temp']-273.15
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        wind=data['wind']['speed']*3.6
        epoch_time=data['dt']
        date_time=datetime.fromtimestamp(epoch_time)
        desc=data['weather'][0]['description']
        cloudy=data['clouds']['all']

        time_label.config(text=str(date_time))
        entry2.insert(0,'{:.2f}'.format(temp)+' celcius')
        entry3.insert(0, str(pressure)+' hpa')
        entry4.insert(0, str(humidity) + ' %')
        entry5.insert(0, '{:.2f}'.format(wind) + ' km/h')
        entry6.insert(0, str(cloudy) + ' %')
        entry7.insert(0, str(desc))

    else:
        mb.showerror('Error','City Not Found. Enter a valid city name.')
        entry1.delete(0,END)

def reset():
    entry1.delete(0,END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    time_label.config(text='')

title=Label(window, text='Weather Detection & Forecast',width=45,height=3,fg='black',bg='sky blue',font='Ivy 20 bold ')
title.place(x=20,y=15)

label1=Label(window, text='Enter City:',width=30,height=1,bg='sky blue',fg='black',font='Ivy 14')
label1.place(x=5, y=120)

time_label=Label(window,text='',bg='sky blue',font='Ivy 14 bold',fg='white')
time_label.place(x=580, y=90)

b1=Button(window, text='Get Weather', width=10, height=1, fg='black', bg='green',command=get_weather)
b1.place(x=400, y=160)

l2=Label(window, text='Temperature:',width=30,height=1,bg='sky blue',fg='black',font='Ivy 14')
l2.place(x=5, y=200)

l3=Label(window, text='Pressure:',width=30,height=1,bg='sky blue',fg='black',font='Ivy 14')
l3.place(x=5, y=240)

l4=Label(window, text='Humidity:',width=30,height=1,bg='sky blue',fg='black',font='Ivy 14')
l4.place(x=5, y=280)

l5=Label(window, text='Wind:',width=30,height=1,bg='sky blue',fg='black',font='Ivy 14')
l5.place(x=5, y=320)

l6=Label(window, text='Cloudiness:',width=30,height=1,bg='sky blue',fg='black',font='Ivy 14')
l6.place(x=5, y=360)

l7=Label(window, text='Description:',width=30,height=1,bg='sky blue',fg='black',font='Ivy 14')
l7.place(x=5, y=400)

b3=Button(window, text='Reset',width=8,height=1,bg='green',fg='black',command=reset)
b3.place(x=400,y=440)


entry1=Entry(window,width=50,font='Ivy 12')
entry1.place(x=250,y=120)

entry2=Entry(window,width=50,font='Ivy 12')
entry2.place(x=250,y=200)

entry3=Entry(window,width=50,font='Ivy 12')
entry3.place(x=250,y=240)

entry4=Entry(window,width=50,font='Ivy 12')
entry4.place(x=250,y=280)

entry5=Entry(window,width=50,font='Ivy 12')
entry5.place(x=250,y=320)

entry6=Entry(window,width=50,font='Ivy 12')
entry6.place(x=250,y=360)

entry7=Entry(window,width=50,font='Ivy 12')
entry7.place(x=250,y=400)

window.mainloop()
