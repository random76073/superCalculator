import tkinter as tk
from _tkinter import TclError
import tkinter.messagebox as tk_message
def divmodMain():
	tkint = tk.Tk()
	tkint.geometry('180x100+500+500')
	tkint.title('带余除法')
	tk.Label(tkint, text='输入格式：\n被除数， 除数\t别输错了').pack(side='top')
	suanshis = tk.Entry(tkint)
	suanshis.pack(side='top', pady=5)

	def calculator():
		nonlocal tkint
		try:
			dm = tuple((int(p) for p in suanshis.get().split(', ')))
			resd, resm = divmod(dm[0], dm[1])
		except TclError:
			tk_message.showerror('', '输入错误')
			tkint.destroy()
		except TypeError:
			tk_message.showerror('', '这不是个数。')
			tkint.destroy()
		except NameError:
			tk_message.showerror('', '这不是个表达式。')
			tkint.destroy()
		except ValueError:
			tk_message.showerror('', '这不是个表达式。')
			tkint.destroy()
		except Exception as e:
			print(e)
			tk_message.showerror('', '我也不知道哪错了，反正就是错了。')
			tkint.destroy()
		else:
			string = '计算成功， {0}/{1}={2}……{3}'.format(dm[0], dm[1], resd, resm)
			tkint.destroy()
			tk_message.showinfo('计算成功', string)
	tk.Button(tkint, text='确定', command=calculator).pack(side='bottom', pady=5)
