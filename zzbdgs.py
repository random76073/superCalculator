import tkinter as tk
def zzbdsMain():
    tkint = tk.Tk()
    v = tk.StringVar(tkint)
    tkint.title('中缀表达式求值')

    def calculator():
        nonlocal tkint
        nonlocal entry
        nonlocal v
        tkint.destroy()
        tkint = tk.Tk()
        tkint.title('计算结果')
        try:
            zzbds = v.get()
            res = eval(zzbds)
        except TypeError:
            result = tk.Label(tkint, text="输入有误，程序崩溃")
            result.pack()
        except SyntaxError:
            result = tk.Label(tkint, text="是不是有些字符没切到英文输入？")
            result.pack()
        except NameError:
            result = tk.Label(tkint, text='这是个表达式？？')
            result.pack()
        except ZeroDivisionError:
            result = tk.Label(tkint, text='不能使用0作为除数！')
            result.pack()
        except:
            result = tk.Label(tkint, text="我也不知道错哪了，反正就是错了。")
            result.pack()
        else:
            result = tk.Label(tkint, text="计算结束，{0}={1}".format(zzbds, res), cursor="heart")
            result.pack()
        finally:
            stop = tk.Button(tkint, text="结束", command=tkint.destroy)
            stop.pack()
    top = tk.Label(tkint, text="输入一个中缀表达式（注意要切换到英文输入法， 整除用//， 取模用%，虚数单位用j表示）", cursor="circle")
    top.pack()
    entry = tk.Spinbox(tkint, textvariable=v)
    entry.pack()
    t = tk.Button(tkint, text="计算", command=calculator)
    t.pack()
    tk.mainloop()
