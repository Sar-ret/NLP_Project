from datetime import datetime
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def Show():
    result.delete(1.0, 'end')
    month=comboMon.get()
    day=comboDay.get()
    myYear=comboYear.get()
    name=inputName.get()
    now=datetime.now()
    next = datetime(now.year, int(month), int(day))
    mybirth=datetime(int(myYear),int(month),int(day))

    T=now-mybirth
    age = T.days / 365.25

    if now.month == int(month) and now.day==int(day):
        comming = now-now
    else:
        comming=next-now

    if comming.days < 0 :
        next=datetime(now.year+1, int(month),int(day))
        comming=next-now
    elif comming.days == 0 :
        comming = "*Happy Birthday to you!* :) "

    ans = "Hello " +name + "! you are " + str(int(age)) +" now"+ "\nComming birthday is : " + str(comming)
    result.insert(1.0, ans)

top=tk.Tk()
top.geometry("600x450+760+94")
top.minsize(148, 1)
top.maxsize(1924, 1055)
top.resizable(1, 1)
top.title("Coming Birthday")

label1=tk.Label(top, font="-family {Sitka Small} -size 20 -weight bold",text='''Welcome to our Application''',)
label1.place(relx=0.1, rely=0.022, height=55, width=492)

nameLB=tk.Label(top, font="-family {Sitka Small} -size 9 -weight bold",text='''Input your name:''')
nameLB.place(relx=0.05, rely=0.289, height=30, width=141)
name= tk.StringVar()
inputName=tk.Entry(top, textvariable=name,)
inputName.place(relx=0.27, rely=0.289, height=34, relwidth=0.507)

dateInput=tk.Label(top, font="-family {Sitka Small} -size 9 -weight bold",text='''birth of date:''')
dateInput.place(relx=0.083, rely=0.422, height=30, width=109)

year=tk.IntVar()
year = list(range(1990, 2022))
comboYear = ttk.Combobox(top, values=year)
comboYear.set("Year")
comboYear.place(relx=0.63, rely=0.425, relwidth=0.15)

month= tk.IntVar()
month = list(range(1, 13))
comboMon = ttk.Combobox(top, values=month)
comboMon.set("Month")
comboMon.place(relx=0.45, rely=0.425, relwidth=0.15)

day=tk.IntVar()
day = list(range(1, 32))
comboDay = ttk.Combobox(top, values=day)
comboDay.set("Day")
comboDay.place(relx=0.27, rely=0.425, relwidth=0.15)

summit=tk.Button(top, text='''Show Comming Brithday''', command=Show)
summit.place(relx=0.40, rely=0.544, height=33, width=150)

result=tk.Text(top, wrap=tk.WORD)
result.place(relx=0.18, rely=0.63, height=100, width=400)

top.mainloop()