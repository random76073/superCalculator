# -*-coding: gbk -*-
import tkinter as tk
from zzbdgs import zzbdsMain
from divmod import divmodMain
from figure import figureMain
import tkinter.messagebox as tk_message
from trueOrFalse import tofMain
tki = tk.Tk()
tki.title('superCalculator')
tki.geometry('228x264+304+117')
tki.resizable(False, False)
tk.Label(tki, text='������', cursor='hand2', font='bold 50').pack()
tk.Button(tki, text='��׺���\nʽ��ֵ', command=zzbdsMain).pack(side='left', padx=20, pady=50)
tk.Button(tki, text='�������', command=divmodMain).pack(side='right', padx=20, pady=40)
tk.Button(tki, text='ͼ��\n����', command=figureMain).pack(side='bottom', pady=10)
tk.Button(tki, text='�жϱ��\nʽ��٣�˵���˾��Ǳȴ�С��(��ʾ���ϵ��or, ���ϵ��and�� ���ϵ��not)', command=tofMain)
if_top = 1
def change_top():
	global if_top
	tki.attributes('-topmost', if_top % 2)
	if_top += 1
def cl():
	if tk_message.askokcancel('', 'ȷ���رգ�'):
		tki.destroy()
		quit()
		exit()
		quit(exit(quit(exit(quit(exit(quit(exit(quit(exit())))))))))
tki.protocol('WM_DELETE_WINDOW', cl)
tki.iconbitmap('I:/ϡ�еĽ����Ŀռ�/supercalculator/supercalculator.ico')
menu = tk.Menu(tki)
Setting = tk.Menu(menu, tearoff=False)
Setting.add_checkbutton(label='���ִ�����ǰ', command=change_top)
menu.add_cascade(menu=Setting, label='Setting')
tki.config(menu=menu)
RCmenu = tk.Menu(tki, tearoff=False)
RCmenu.add_command(label='Exit', command=quit)
RCmenu.add_separator()
fsQ = 0
def fullscreen():
	global fsQ
	fsQ += 1
	tki.attributes('-fullscreen', fsQ % 2)
def RCP(event):
	RCmenu.post(event.x_root, event.y_root)
RCmenu.add_checkbutton(label='ȫ��', command=fullscreen)
tki.bind('<Button-3>', RCP)

tki.mainloop()

