import tkinter
from tkinter import *
from nltk.corpus import wordnet

window = tkinter.Tk()
window.geometry("600x500")
window.title('Dictionary')

def word():
    txt.delete("1.0", "end")
    synonyms = []
    antonyms = []
    word = textInput.get()
    syns = wordnet.synsets(word)
    txt.insert(END,"Definition: " + syns[0].definition()+"\n")
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    synonyms = list(dict.fromkeys(synonyms))
    antonyms = list(dict.fromkeys(antonyms))
    txt.insert(END, "Example: ")
    for ex in syns[0].examples():
        txt.insert(END, ex+",")
    txt.insert(END, "\nSynonyms: ")
    for sy in synonyms:
        txt.insert(END, sy+",")
    txt.insert(END, "\nAntonyms: ")
    for an in antonyms:
        txt.insert(END, an+",")



frame = tkinter.Frame(window, width=300, height=40)
frame.place(x=50, y=10)

textInput = StringVar()

entry = tkinter.Entry(frame, width=30, textvariable = textInput)
entry.pack(side="left")


Btn = tkinter.Button(frame, text="Find", width=5, command=word)
Btn.pack(side="right", padx=5)


_txt = tkinter.Frame(window, width=350, height=200)
_txt.place(x=20, y=40)


scroll_bar = tkinter.Scrollbar(_txt)
scroll_bar.pack(side="right", fill=tkinter.Y)


txt = tkinter.Text(_txt, width=200, height=18)
txt.pack(side="bottom", pady=15)
txt.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=txt.yview)

window.mainloop()
