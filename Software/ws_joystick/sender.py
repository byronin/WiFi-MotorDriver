# ********* >  pip install websocket-client
import websocket
from tkinter import *
import threading
import time
import os

UI = Tk()
UI.title('WS Joystcik - Ronin')
UI.geometry('680x400')
UI.config(bg="grey")


data_param = open("IP_param.txt")
saw = data_param.read()
data_param.close()

ws = websocket.WebSocket()
ws.connect(saw)

ws.send("Hello, Car")

direction = StringVar()
direction.set("stop")
def send_car():
    while True:

        if direction.get() == "forward":
            ws.send("F:"+str(speed_slide.get())+"\n")
        elif direction.get() == "backward":
            ws.send("B:"+str(speed_slide.get())+"\n")
        elif direction.get() == "left":
            ws.send("L:"+str(turn_slide.get())+"\n")
        elif direction.get() == "right":
            ws.send("R:"+str(turn_slide.get())+"\n")
        elif direction.get() == "stop":
            ws.send("STOP\n")
        time.sleep(0.15)

thread_sender = threading.Thread(target=send_car)
thread_sender.start()



def d_forward(event):
   direction.set("forward")

def d_backward(event):
   direction.set("backward")

def d_left(event):
   direction.set("left")

def d_right(event):
   direction.set("right")

def exit_ws():
    ws.close()
def reconnect():
    ws = websocket.WebSocket()
    ws.connect(saw)

connect_button = Button(UI, text="RECONNECT",command=lambda :reconnect,height=2, width=12)
connect_button.place(x=490,y=20)

disconnect_button = Button(UI, text="DISCONNECT",command=exit_ws,height=2, width=12)
disconnect_button.place(x=360,y=20)

forward_photo = PhotoImage(file='forward.png')
forward_button = Button(UI,image = forward_photo, command=lambda:direction.set("stop"),borderwidth=0,height=100, width=78,bg="grey")
forward_button.place(x=100,y=100)
forward_button.bind('<Button-1>', d_forward)



backward_photo = PhotoImage(file='backward.png')
backward_button = Button(UI,image = backward_photo , command=lambda:direction.set("stop"),borderwidth=0,height=100, width=78,bg="grey")
backward_button.place(x=100,y=250)
backward_button.bind('<Button-1>', d_backward)


left_photo = PhotoImage(file='left.png')
left_button = Button(UI,image = left_photo,  command=lambda:direction.set("stop"),borderwidth=0,height=78, width=100,bg="grey")
left_button.place(x=10,y=185)
left_button.bind('<Button-1>', d_left)


right_photo = PhotoImage(file='right.png')
right_button = Button(UI, image=right_photo,  command=lambda:direction.set("stop"), borderwidth=0, height=78, width=100, bg="grey")
right_button.place(x=170, y=185)
right_button.bind('<Button-1>', d_right)


speed_label = Label(UI, text="Speed:", height=1, width=5, bg="grey", font="Candara")
speed_label.place(x=320, y=240)

speed_slide = Scale(UI, from_=0, to=100, orient=HORIZONTAL, length=300, tickinterval=10, width=10, bg="grey")
speed_slide.set(50)
speed_slide.place(x=320, y=270)


turn_label = Label(UI, text="Soft Rotation:", height=1, width=10, bg="grey", font="Candara")
turn_label.place(x=320, y=110)

turn_slide = Scale(UI, from_=0, to=100, orient=HORIZONTAL, length=300, tickinterval=10, width=10, bg="grey")
turn_slide.set(50)
turn_slide.place(x=320, y=140)
UI.mainloop()