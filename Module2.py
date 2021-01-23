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


def show():
    result.delete(1.0, 'end')
    month = comboMonth.get()
    day = comboDay.get()
    year = comboYear.get()
    name = inputName.get()
    now = datetime.now()

    if name == "":
        result.insert(1.0, "Please input your name!")
        return False
    try:
        next = datetime(now.year, int(month), int(day))
        mybirth = datetime(int(year), int(month), int(day))
    except ValueError:
        result.insert(1.0, "Please select your Birthday!")
        return False

    T = now - mybirth
    age = T.days / 365.25

    if now.month == int(month) and now.day == int(day):
        coming = now-now
    else:
        coming = next-now

    if coming.days < 0:
        next = datetime(now.year+1, int(month), int(day))
        coming = next-now
    elif coming.days == 0:
        coming = "*Happy Birthday to you!* :) "

    ans = "Hello " + name + "! you are " + str(int(age)) +" now"+ "\nYour coming birthday is : " + str(coming.days) + " days"
    result.insert(1.0, ans)


def create_window(width, height, title):
    win = tk.Tk()
    win.geometry("{}x{}+760+94".format(width, height))
    win.title("{}".format(title))
    return win


def create_label(win, _font, _text):
    label = tk.Label(win, font=_font, text=_text)
    return label


def placeElement(element, _relx, _rely, _relwidth, _relheight, _anchor=""):
    if _anchor == "":
        element.place(relx=_relx, rely=_rely, relwidth=_relwidth, relheight=_relheight)
    else:
        element.place(relx=_relx, rely=_rely, relwidth=_relwidth, relheight=_relheight, anchor=_anchor)

def placeLabel(element, _relx, _rely,  _anchor=""):
    if _anchor == "":
        element.place(relx=_relx, rely=_rely)
    else:
        element.place(relx=_relx, rely=_rely, anchor=_anchor)


def create_input(win):
    input = tk.Entry(win, textvariable=tk.StringVar())
    return input


def create_select(win, min_nb, max_nb, title):
    year = list(range(min_nb, max_nb))
    combo_box = ttk.Combobox(win, values=year)
    combo_box.set("{}".format(title))
    return combo_box


def show_output(win, _fg=""):
    result = tk.Text(win, fg=_fg)
    return result


def create_button(win, _text, _command=""):
    button = tk.Button(win, text=_text, command=_command)
    return button

win = create_window(600, 500, "Birthday")
# Header
Label1 = create_label(win, "-family {Sitka Small} -size 20 -weight bold", 'Welcome to our Application')
placeLabel(Label1, 0.5, 0.1, "center")
# label name
nameLB = create_label(win, "-family {Sitka Small} -size 10 -weight bold", 'Input your name:')
placeLabel(nameLB, 0.140, 0.29, 'center')
# Get input
inputName = create_input(win)
placeElement(inputName, 0.5, 0.289, 0.5, 0.07, 'center')
# Label show
dateInput = create_label(win, "-family {Sitka Small} -size 9 -weight bold", 'Birth of date:')
placeElement(dateInput, 0.140, 0.4, 0.30, 0.109, 'center')
# select Year
comboYear = create_select(win, 1990, 2022, 'Year')
placeElement(comboYear, 0.7, 0.4, 0.15, 0.05, 'center')
# select Month
comboMonth = create_select(win, 1, 13, 'Month')
placeElement(comboMonth, 0.5, 0.4, 0.15, 0.05, 'center')
# select Day
comboDay = create_select(win, 1, 32, 'Day')
placeElement(comboDay, 0.3, 0.4, 0.15, 0.05, 'center')
# Button click
summit = create_button(win, 'Show Coming Birthday', show)
placeElement(summit, 0.5, 0.544, 0.3, 0.06, 'center')
# Output
result = show_output(win, "red")
placeElement(result, 0.5, 0.63, 0.55, 0.1, 'center')

win.mainloop()

