from tkinter import *
from tkinter import messagebox
import keyboard
from pynput.keyboard import Controller
from pynput.keyboard import Key, Listener
import logging


root = Tk()



L1 = Label(root)
L1.place(x=10,y=10,w=740,h=280)

L2 = Label(root,)
L2.place(x=10,y=320,w=740,h=260)


#bs=StringVar()
def on():
    while True:
            try:
                if keyboard.on_press_key("q", lambda _:bn.configure(background='red')):
                    #elif on_key_release(lambda _:bn.configure(background='whie')):
                        #else:
                    #bn.configure(foreground='red')
                    break  # finishing the loop
            except:
                 break
       
            

        
bn = Button(L1, text = 'q', bd = '5', command=on,relief=GROOVE)
bn.place(x=50,y=90,w=40,h=30)    


   
b = Button(L1, text = 'Esc',font=('Helvetica', 11, 'bold'),bd = '5', relief=GROOVE)
b.place(x=10,y=10,w=40,h=30)

btn = Button(L1, text = 'F1', bd = '5', relief=GROOVE)
btn.place(x=50,y=10,w=40,h=30)
btn = Button(L1, text = 'F2', bd = '5', relief=GROOVE)
btn.place(x=90,y=10,w=40,h=30)
btn = Button(L1, text = 'F3', bd = '5', relief=GROOVE)
btn.place(x=130,y=10,w=40,h=30)
btn = Button(L1, text = 'F3', bd = '5', relief=GROOVE)
btn.place(x=170,y=10,w=40,h=30)
btn = Button(L1, text = 'F4', bd = '5', relief=GROOVE)
btn.place(x=210,y=10,w=40,h=30)
btn = Button(L1, text = 'F5', bd = '5', relief=GROOVE)
btn.place(x=250,y=10,w=40,h=30)
btn = Button(L1, text = 'F6', bd = '5', relief=GROOVE)
btn.place(x=290,y=10,w=40,h=30)

btn = Button(L1, text = 'F7', bd = '5', relief=GROOVE)
btn.place(x=330,y=10,w=40,h=30)

btn = Button(L1, text = 'F8', bd = '5', relief=GROOVE)
btn.place(x=370,y=10,w=40,h=30)

btn = Button(L1, text = 'F9', bd = '5', relief=GROOVE)
btn.place(x=410,y=10,w=40,h=30)

btn = Button(L1, text = 'F10', bd = '5', relief=GROOVE)
btn.place(x=450,y=10,w=40,h=30)

btn = Button(L1, text = 'F11', bd = '5', relief=GROOVE)
btn.place(x=490,y=10,w=40,h=30)

btn = Button(L1, text = 'F12', bd = '5', relief=GROOVE)
btn.place(x=530,y=10,w=40,h=30)

btn = Button(L1, text = 'PriSc', bd = '5', relief=GROOVE)
btn.place(x=570,y=10,w=40,h=30)

btn = Button(L1, text = 'ScrlLock', bd = '5', relief=GROOVE)
btn.place(x=610,y=10,w=70,h=30)

btn = Button(L1, text = 'Pause', bd = '5', relief=GROOVE)
btn.place(x=680,y=10,w=50,h=30)

### o sequence
btn = Button(L1, text = '~', bd = '5', relief=GROOVE)
btn.place(x=10,y=50,w=40,h=30)

btn = Button(L1, text = '1', bd = '5', relief=GROOVE)
btn.place(x=50,y=50,w=40,h=30)

btn = Button(L1, text = '2', bd = '5', relief=GROOVE)
btn.place(x=90,y=50,w=40,h=30)

btn = Button(L1, text = '3', bd = '5', relief=GROOVE)
btn.place(x=130,y=50,w=40,h=30)

btn = Button(L1, text = '4', bd = '5', relief=GROOVE)
btn.place(x=170,y=50,w=40,h=30)



btn = Button(L1, text = '5', bd = '5', relief=GROOVE)
btn.place(x=210,y=50,w=40,h=30)

btn = Button(L1, text = '6', bd = '5', relief=GROOVE)
btn.place(x=250,y=50,w=40,h=30)

btn = Button(L1, text = '7', bd = '5', relief=GROOVE)
btn.place(x=290,y=50,w=40,h=30)

btn = Button(L1, text = '8', bd = '5', relief=GROOVE)
btn.place(x=330,y=50,w=40,h=30)

btn = Button(L1, text = '9', bd = '5', relief=GROOVE)
btn.place(x=370,y=50,w=40,h=30)

btn = Button(L1, text = '0', bd = '5', relief=GROOVE)
btn.place(x=410,y=50,w=40,h=30)

btn = Button(L1, text = '-', bd = '5', relief=GROOVE)
btn.place(x=450,y=50,w=40,h=30)

btn = Button(L1, text = '=', bd = '5', relief=GROOVE)
btn.place(x=490,y=50,w=40,h=30)

btn = Button(L1, text = 'BackSP', bd = '5', relief=GROOVE)
btn.place(x=530,y=50,w=60,h=30)

btn = Button(L1, text = 'Insert', bd = '5', relief=GROOVE)
btn.place(x=590,y=50,w=50,h=30)

btn = Button(L1, text = 'Home',font=('Helvetica', 10, 'bold'), bd = '5', relief=GROOVE)
btn.place(x=640,y=50,w=50,h=30)

btn = Button(L1, text = 'PgUp', bd = '5', relief=GROOVE)
btn.place(x=690,y=50,w=40,h=30)
## keybrd
btn = Button(L1, text = 'Tab',font=('Helvetica', 11, 'bold'), bd = '5', relief=GROOVE)
btn.place(x=10,y=90,w=40,h=30)



btn = Button(L1, text = 'W', bd = '5', relief=GROOVE)
btn.place(x=90,y=90,w=40,h=30)

btn = Button(L1, text = 'E', bd = '5', relief=GROOVE)
btn.place(x=130,y=90,w=40,h=30)

btn = Button(L1, text = 'R', bd = '5', relief=GROOVE)
btn.place(x=170,y=90,w=40,h=30)

btn = Button(L1, text = 'T', bd = '5', relief=GROOVE)
btn.place(x=210,y=90,w=40,h=30)

btn = Button(L1, text = 'Y', bd = '5', relief=GROOVE)
btn.place(x=250,y=90,w=40,h=30)
btn = Button(L1, text = 'U', bd = '5', relief=GROOVE)
btn.place(x=290,y=90,w=40,h=30)
btn = Button(L1, text = 'I', bd = '5', relief=GROOVE)
btn.place(x=330,y=90,w=40,h=30)
btn = Button(L1, text = 'O', bd = '5', relief=GROOVE)
btn.place(x=370,y=90,w=40,h=30)
btn = Button(L1, text = 'P', bd = '5', relief=GROOVE)
btn.place(x=410,y=90,w=40,h=30)
btn = Button(L1, text = '[', bd = '5', relief=GROOVE)
btn.place(x=450,y=90,w=40,h=30)
btn = Button(L1, text = ']', bd = '5', relief=GROOVE)
btn.place(x=490,y=90,w=40,h=30)

btn = Button(L1, text = '|', bd = '5', relief=GROOVE)
btn.place(x=530,y=90,w=40,h=30)

btn = Button(L1, text = 'Del',font=('Helvetica', 10, 'bold'), bd = '5', relief=GROOVE)
btn.place(x=570,y=90,w=40,h=30)

btn = Button(L1, text = 'End',font=('Helvetica', 10, 'bold'),bd = '5', relief=GROOVE)
btn.place(x=610,y=90,w=40,h=30)

btn = Button(L1, text = 'PgDn', bd = '5', relief=GROOVE)
btn.place(x=650,y=90,w=50,h=30)

###Caps lock

btn = Button(L1, text = 'CapsLK', bd = '5', relief=GROOVE)
btn.place(x=10,y=130,w=60,h=30)

btn = Button(L1, text = 'A', bd = '5', relief=GROOVE)
btn.place(x=70,y=130,w=40,h=30)

btn = Button(L1, text = 'S', bd = '5', relief=GROOVE)
btn.place(x=110,y=130,w=40,h=30)

btn = Button(L1, text = 'D', bd = '5', relief=GROOVE)
btn.place(x=150,y=130,w=40,h=30)

btn = Button(L1, text = 'F', bd = '5', relief=GROOVE)
btn.place(x=190,y=130,w=40,h=30)

btn = Button(L1, text = 'G', bd = '5', relief=GROOVE)
btn.place(x=230,y=130,w=40,h=30)

btn = Button(L1, text = 'H', bd = '5', relief=GROOVE)
btn.place(x=270,y=130,w=40,h=30)
btn = Button(L1, text = 'J', bd = '5', relief=GROOVE)
btn.place(x=310,y=130,w=40,h=30)
btn = Button(L1, text = 'K', bd = '5', relief=GROOVE)
btn.place(x=350,y=130,w=40,h=30)
btn = Button(L1, text = 'L', bd = '5', relief=GROOVE)
btn.place(x=390,y=130,w=40,h=30)
btn = Button(L1, text = ';', bd = '5', relief=GROOVE)
btn.place(x=430,y=130,w=40,h=30)
btn = Button(L1, text = ' " ' , bd = '5', relief=GROOVE)
btn.place(x=470,y=130,w=40,h=30)
btn = Button(L1, text = 'Enter', font=('Helvetica', 10, 'bold'),bd = '5', relief=GROOVE)
btn.place(x=510,y=130,w=60,h=30)

## Shift
btn = Button(L1, text = 'Shift',font=('Helvetica', 11, 'bold'), bd = '5', relief=GROOVE)
btn.place(x=10,y=170,w=60,h=30)

btn = Button(L1, text = 'Z', bd = '5', relief=GROOVE)
btn.place(x=70,y=170,w=40,h=30)

btn = Button(L1, text = 'X', bd = '5', relief=GROOVE)
btn.place(x=110,y=170,w=40,h=30)

btn = Button(L1, text = 'C', bd = '5', relief=GROOVE)
btn.place(x=150,y=170,w=40,h=30)

btn = Button(L1, text = 'V', bd = '5', relief=GROOVE)
btn.place(x=190,y=170,w=40,h=30)

btn = Button(L1, text = 'B', bd = '5', relief=GROOVE)
btn.place(x=230,y=170,w=40,h=30)

btn = Button(L1, text = 'N', bd = '5', relief=GROOVE)
btn.place(x=270,y=170,w=40,h=30)
btn = Button(L1, text = 'M', bd = '5', relief=GROOVE)
btn.place(x=310,y=170,w=40,h=30)
btn = Button(L1, text = ',', bd = '5', relief=GROOVE)
btn.place(x=350,y=170,w=40,h=30)
btn = Button(L1, text = '.', bd = '5', relief=GROOVE)
btn.place(x=390,y=170,w=40,h=30)
btn = Button(L1, text = '/', bd = '5', relief=GROOVE)
btn.place(x=430,y=170,w=40,h=30)
btn = Button(L1, text = ' Shift ' , font=('Helvetica', 11, 'bold') , bd ='5' , relief=GROOVE )
btn.place(x=470,y=170,w=70,h=30)


#### Control
btn = Button(L1, text = 'Ctrl',font=('Helvetica', 11, 'bold'), bd = '5', relief=GROOVE)
btn.place(x=10,y=210,w=60,h=30)

btn = Button(L1, text = 'Fn',font=('Helvetica', 11, 'bold'), bd = '5', relief=GROOVE)
btn.place(x=70,y=210,w=40,h=30)

btn = Button(L1, text = 'Xwin', bd = '5', relief=GROOVE)
btn.place(x=110,y=210,w=40,h=30)

btn = Button(L1, text = 'Alt', bd = '5', relief=GROOVE)
btn.place(x=150,y=210,w=40,h=30)

btn = Button(L1, text = ' Space ', bd = '5', relief=GROOVE)
btn.place(x=190,y=210,w=160,h=30)

btn = Button(L1, text = 'B', bd = '5', relief=GROOVE)
btn.place(x=350,y=210,w=40,h=30)

btn = Button(L1, text = 'N', bd = '5', relief=GROOVE)
btn.place(x=390,y=210,w=40,h=30)
btn = Button(L1, text = 'M', bd = '5', relief=GROOVE)
btn.place(x=430,y=210,w=40,h=30)
btn = Button(L1, text = ',', bd = '5', relief=GROOVE)
btn.place(x=470,y=210,w=40,h=30)
btn = Button(L1, text = '.', bd = '5', relief=GROOVE)
btn.place(x=510,y=210,w=40,h=30)
btn = Button(L1, text = '/', bd = '5', relief=GROOVE)
btn.place(x=550,y=210,w=40,h=30)
btn = Button(L1, text = 'Ctrl' , font=('Helvetica', 11, 'bold') , bd ='5' , relief=GROOVE )
btn.place(x=590,y=210,w=70,h=30)



    























## about Tkinter 
root.title("TYPE Learner")
root.configure(background='#40E0D0')
root.geometry("760x590")
root.resizable(0,0)
root.mainloop()


























'''L2 = Label(root, text='Login')
L2.pack() 

L3 = Label(root, text = "Username:")
L3.pack( side = LEFT, padx = 5, pady = 10)
username = StringVar()
E1 = Entry(root, textvariable = username, width = 40)
E1.pack ( side = LEFT)

L4 = Label(root, text = "Password:")
L4.pack( side = LEFT, padx = 5, pady = 10)
password = StringVar() 
E2 = Entry(root, textvariable = password, show = "*", width = 40)    
E2.pack( side = LEFT)'''

