
from tkinter import *
import time 

window = TK()
window.title('Digital Clock')
window.geometry('600*400')

def myTime():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime("%p")
    myText = hour + ":" + minute + ":" + second + ":" + am_pm
    myText2 = day + "," + zone
    day = time.strftime("%A")
    zone = time.strftime("%Z")
    myLabel.config(text=myText)
    myLabel2.config(text=myText2)
    myLabel.after(1000, myTime)
    
    
myLabel = Label(window, text="hello world", font=('Arial', 72), fg='white', bg='green')
myLabel.pack()
myLabel2 = Label(window, text="",font=('Arial', 72))

window.mainloop()