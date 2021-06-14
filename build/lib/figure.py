import tkinter as tk
import tkinter.ttk as ttk
from oftenUser import switch
import tkinter.messagebox as tk_message
import tkinter.simpledialog as tk_ask

def figureMain():
	tkint = tk.Tk()
	tkint.title('图形计算')
	tk.Label(tkint, text='请选择一种图形：').pack()
	choose = ttk.Combobox(tkint, values=('circle', 'oval', 'square', 'triangle', 'parallelogram', 'rectangle', 'trapezoid', 'cube', 'cuboid', 'cylinder', 'cone', 'roundTable', 'ball'))
	choose.pack()
	formulac = None
	formulas = None
	formulav = None
	figure = 0
	argc = []
	args = []
	argv = []

	def decide():
		nonlocal formulac
		nonlocal formulas
		nonlocal formulav
		nonlocal choose
		nonlocal figure
		nonlocal argc
		nonlocal args
		nonlocal argv
		argc.clear()
		args.clear()
		argv.clear()
		figure = choose.get()
		tkint.destroy()
		for case in switch(figure):
			if case('circle'):
				formulac = '2*{0}*{1}'
				formulas = '{0}*{1}*{1}'
				argc.extend(['pi', 'r'])
				args.extend(['pi', 'r'])
				break
			if case('oval'):
				formulas = '{0}*{1}*{2}'
				args.extend(['pi', 'a', 'b'])
				break
			if case('square'):
				formulac = '{0}*4'
				formulas = '{0}*{0}'
				argc.append('a')
				args.append('a')
				break
			if case('triangle'):
				formulas = '{0}*{1}/2'
				args.extend(['a', 'h'])
				break
			if case('parallelogram'):
				formulas = '{0}*{1}'
				args.extend(['a', 'h'])
				break
			if case('rectangle'):
				formulac = '({0}+{1})*2'
				formulas = '{0}*{1}'
				argc.extend(['a', 'b'])
				args.extend(argc)
				break
			if case('trapezoid'):
				formulas = '({0}+{1})*{2}/2'
				args.extend(['a', 'b', 'h'])
				break
			if case('cube'):
				formulac = '12*{0}'
				formulas = '6*{0}*{0}'
				formulav = '{0}*{0}*{0}'
				argc.append('a')
				args.append('a')
				argv.append('a')
				break
			if case('cuboid'):
				formulac = '4*({0}+{1}+{2})'
				formulas = '2*({0}*{1}+{1}*{2}+{2}*{0})'
				formulav = '{0}*{1}*{2}'
				argc.extend(['a', 'b', 'h'])
				args.extend(argc)
				argv.extend(args)
				break
			if case('cylinder'):
				# {0}=pi; {1}=r; {2}=h
				formulas = '2*{0}*{1}*({2}+{1})'
				formulav = '{0}*{1}*{1}*{2}'
				args.extend(['pi', 'r', 'h'])
				argv.extend(args)
				break
			if case('cone'):
				# {0}=pi; {1}=r; {2}=h
				formulas = '{0}*{1}*({2}**2+{1}**2)**0.5+{0}*{1}*{1}'
				formulav = '({0}*{1}**2*{2})/3'
				args.extend(['pi', 'r', 'h'])
				argv.extend(args)
				break
			if case('roundTable'):
				# {0}=pi; {1}=r; {2}=R; {3}=h; before:π(r²+R²+Rl+rl), l=((R-r)**2+h**2)**0.5
				formulas = '{0}*({1}**2+{2}**2+{2}*(({2}-{1})**2+{3}**2)**0.5+{1}*(({2}-{1})**2+{3}**2)**0.5)'
				formulav = '{0}*{3}*({2}**2+{1}**2+{2}*{1})'
				args.extend(['pi', 'r', 'R', 'h'])
				argv.extend(args)
				break
			if case('ball'):
				formulas = '4*{0}*{1}**2'
				formulav = '({0}*{1}**3)*4/3'
				args.extend(['pi', 'R'])
				argv.extend(args)
				break
			if case():
				tk_message.showerror('错误', '这不是可选择图形！')
				tkint.destroy()
		calculator()
	optionw = None

	def askc():
		arg = []
		for i in range(len(argc)):
			arg.append(tk_ask.askfloat('输入参数', '请输入{0}值：'.format(argc[i])))
		if len(argc) == 1:
			res = eval(formulac.format(arg[0]))
		elif len(argc) == 2:
			res = eval(formulac.format(arg[0], arg[1]))
		elif len(argc) == 3:
			res = eval(formulac.format(arg[0], arg[1], arg[2]))
		else:
			res = eval(formulac.format(arg[0], arg[1], arg[2], arg[3]))
		tk_message.showinfo('', '计算成功，结果={0}'.format(res))

	def asks():
		arg = []
		for i in range(len(args)):
			arg.append(tk_ask.askfloat('输入参数', '请输入{0}值：'.format(args[i])))
		if len(args) == 1:
			res = eval(formulas.format(arg[0]))
		elif len(args) == 2:
			res = eval(formulas.format(arg[0], arg[1]))
		elif len(args) == 3:
			res = eval(formulas.format(arg[0], arg[1], arg[2]))
		else:
			res = eval(formulas.format(arg[0], arg[1], arg[2], arg[3]))
		tk_message.showinfo('', '计算成功，结果={0}'.format(res))

	def askv():
		arg = []
		for i in range(len(argv)):
			arg.append(tk_ask.askfloat('输入参数', '请输入{0}值：'.format(argv[i])))
		if len(argv) == 1:
			res = eval(formulav.format(arg[0]))
		elif len(argv) == 2:
			res = eval(formulav.format(arg[0], arg[1]))
		elif len(argv) == 3:
			res = eval(formulav.format(arg[0], arg[1], arg[2]))
		else:
			res = eval(formulav.format(arg[0], arg[1], arg[2], arg[3]))
		tk_message.showinfo('', '计算成功，结果={0}'.format(res))

	def calculator():
		nonlocal formulac
		nonlocal formulas
		nonlocal formulav
		nonlocal optionw
		optionw = tk.Tk()
		optionw.title('你要求什么？')
		if formulac is not None:
			tk.Button(optionw, text='求\n周\n长\n(\n棱\n长\n和\n)', command=askc).pack(side='left', fill='y')
		if formulav is not None:
			tk.Button(optionw, text='求\n体\n积', command=askv).pack(side='right', fill='y')
		if formulas is not None:
			tk.Button(optionw, text='求面积（表面积）', command=asks).pack(side='bottom', fill='x')
		tk.Label(optionw, text=figure, font='bold 50').pack(side='top', fill='x', expand='yes')
	tk.Button(tkint, text='确定', command=decide).pack()
