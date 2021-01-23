import tkinter as tk
from tkinter import *
from nltk.corpus import wordnet


def find_synonyms():
    synonym = []
    output.delete("1.0", "end")
    word = getWord.get()
    if word:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonym.append(l.name())

        synonym = list(set(synonym))
        for l in synonym:
                if l:
                    output.insert(END, l+ ",")
                else:
                    output.insert(END, "Synonyms is not exist!")
    else:
        output.insert(END, "Please input the word!")

def find_antonyms():
    antonyms = []
    output.delete("1.0", "end")
    word = getWord.get()
    if word:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    if l.antonyms()[0].name():
                        antonyms.append(l.antonyms()[0].name())
    else:
        output.insert(END, "Please input the word!")

    antonyms = list(set(antonyms))
    for a in antonyms:
        output.insert(END, a + "\n")


def find_def():
    output.delete("1.0", "end")
    word = getWord.get()
    if word:
        syns = wordnet.synsets(word)
        output.insert(END,syns[0].definition()+"\n")
    else:
        output.insert(END, "Please input the word!")

def find_exam():
    output.delete("1.0", "end")
    word = getWord.get()
    if word:
        syns = wordnet.synsets(word)
        ex = syns[0].examples()
        for e in ex:
            output.insert(END, str(e) + "\n")
    else:
        output.insert(END, "Please input the word!")


def create_window(width, height, title):
    win = tk.Tk()
    win.geometry("{}x{}+760+94".format(width, height))
    win.title("{}".format(title))
    return win

def create_label(win, _font, _text):
    label = tk.Label(win, font=_font, text=_text)
    return label


def placeElement(element, _relx, _rely, _relwidth=0, _relheight=0, _anchor=""):
    if _anchor == "":
        element.place(relx=_relx, rely=_rely, relwidth=_relwidth, relheight=_relheight)
    else:
        element.place(relx=_relx, rely=_rely, relwidth=_relwidth, relheight=_relheight, anchor=_anchor)

def placeLabel(element, _relx, _rely, _anchor=""):
    if _anchor == "":
        element.place(relx=_relx, rely=_rely,)
    else:
        element.place(relx=_relx, rely=_rely, anchor=_anchor)

def create_input(win):
    input = tk.Entry(win, textvariable=tk.StringVar())
    return input

def show_output(win, _fg=""):
    result = tk.Text(win, fg=_fg)
    return result


def create_button(win, _text, _command=""):
    button = tk.Button(win, text=_text, command=_command)
    return button

win = create_window(600, 500, 'Dictionary')
# tiltle
label1 = create_label(win, "-family {Sitka Small} -size 20 -weight bold", 'Welcome to our dictionary application')
placeLabel(label1, 0.5, 0.1, 'center')
#Get input word
getWord = create_input(win)
placeElement(getWord, 0.5, 0.24, 0.4, 0.07, 'center')
# Definition
definition = create_button(win, 'Definition', find_def)
placeElement(definition, 0.1, 0.4, 0.2, 0.07)
# Example
example = create_button(win, 'Example', find_exam)
placeElement(example, 0.32, 0.4, 0.2, 0.07)
# Synonym
synonym = create_button(win, 'Synonym' , find_synonyms)
placeElement(synonym, 0.54, 0.4, 0.2, 0.07)
# Antonym
antonym = create_button(win, 'Antonym', find_antonyms)
placeElement(antonym, 0.76, 0.4, 0.2, 0.07)
# Label show word
label2 = create_label(win, "-family {Sitka Small} -size 12 -weight bold", 'OUTPUT')
placeLabel(label2, 0.5, 0.54, 'center')
# Output
output = show_output(win, "black")
placeElement(output, 0.5, 0.7, 0.6, 0.25, 'center')

win.mainloop()

