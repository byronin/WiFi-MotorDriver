import os
from tkinter import *
import socket
import networkscan
import threading
import time

UI = Tk()
UI.title('WS Scanner - Ronin')
UI.geometry('680x300')
UI.config(bg="grey")

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(('google.com', 0))

#IPAddr=s.getsockname()[0]

usable_ip = ["First You need scan"]

scan_flag = StringVar()
scan_flag.set("STOP")

def drop_list_updater():
    drop_list["menu"].delete(0, "end")
    for item in usable_ip:
        drop_list["menu"].add_command(
            label=item,
            command=lambda value=item: clicked.set(value)
        )

def print_box(Message):
    text_box.insert("end", Message + "\n")
    text_box.see("end")
    UI.update()


def port_input():
    inp = port_box.get(1.0, "end-1c")
    print_box("PORT:"+inp)
    return inp

def scan_ws():
    while True:
        if scan_flag.get() == "RUN":
            clicked.set("Select Usable ıp")
            usable_ip.clear()
            drop_list_updater()

            if __name__ == '__main__':
                print_box(IPAddr)
                x = IPAddr.split(".")
                my_network = x[0] + "." + x[1] + "." + x[2] + "." + "0/24"

                my_scan = networkscan.Networkscan(my_network)

                print_box("Network to scan: " + str(my_scan.network))
                print_box("Prefix to scan: " + str(my_scan.network.prefixlen))
                print_box("Number of hosts to scan: " + str(my_scan.nbr_host))
                print_box("Scanning hosts...")
                my_scan.run()
                print_box("List of hosts found:")

                c = 0
                if port_input() != "":
                  s_port = port_input()
                else:
                    s_port = "8080"
                    port_box.insert("end",s_port )
                    port_box.see("end")
                    UI.update()


                for i in my_scan.list_of_hosts_found:
                    print_box(i)
                    if scan_flag.get() == "RUN":
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        conn = s.connect_ex((i, int(s_port)))

                        if (conn == 0):
                            print_box('Usable Port : ' + i)
                            usable_ip.append(i)
                            drop_list_updater()

                            c = +1
                print_box("Number of hosts found: " + str(my_scan.nbr_host_found))
                scan_flag.set("STOP")


thread_scan = threading.Thread(target=scan_ws)
thread_scan.start()



page_flag = StringVar()
page_flag.set("page1")


def change_page():
    os.system('sender.py')

thread_page = threading.Thread(target=change_page)


def ws_ıp():
    x = IPAddr.split(".")
    y = str(clicked.get()).split(".")
    if x[0] == y[0]:
        try:
            if os.path.exists("IP_param.txt") and os.path.isfile("IP_param.txt"):
                os.remove("IP_param.txt")
            else:
                print_box("error IP remove")

            IP_config = open("IP_param.txt", "a")
            IP_config.write("ws://" + str(clicked.get()) + ":" + port_input() + "/")
            IP_config.close()
            thread_page.start()
            time.sleep(2)
            os._exit(0)
        except IOError:
            print_box("error IP write")
        finally:
            IP_config.close()
    else:
        print_box("**WARNING**Select IP or Scan again")
    IP_config.close()

text_box = Text(UI , height=10, width=40)
text_box.pack(side=LEFT,expand=True)
text_box.place(x=330,y=10)
text_box.config(bg='#D9D8D7')
sb_ver = Scrollbar(UI , orient=VERTICAL)
sb_ver.pack(side=RIGHT, fill=Y)
text_box.config(yscrollcommand=sb_ver.set)
sb_ver.config(command=text_box.yview)

clicked = StringVar()
clicked.set("Select Usable IP.")

drop_list = OptionMenu(UI, clicked, *usable_ip)
drop_list.config(height=1,width=18)
drop_list.place(x=30,y=10)

scan_button = Button(UI, text="Scan",command=lambda:scan_flag.set("RUN"),height=2, width=12)
scan_button.place(x=230,y=10)

connect_button = Button(UI, text="Connect",command=lambda:ws_ıp(),height=2, width=12)
connect_button.place(x=230,y=72)

stopscan_button = Button(UI, text="Stop Scan",command=lambda:scan_flag.set("STOP"),height=2, width=12)
stopscan_button.place(x=230,y=133)

port_box = Text(UI,height=1,width=5)
port_box.place(x=32,y=51)
port_button = Button(UI, text="Cahange PORT",command=port_input,height=1, width=12)
port_button.place(x=81,y=50)

github_photo = PhotoImage(file='github.png')
github_button = Button(UI, image=github_photo, borderwidth=0, height=78, width=200, bg="grey")
github_button.place(x=10, y=92)

UI.mainloop()
