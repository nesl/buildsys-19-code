"""
    This file contains the necessary user interface.
"""
from tkinter import *

def selectIntention(intentions):
    window = Tk()
    window.title('Remedial Actions Intention')
    window.geometry('350x200')
    lbl = Label(window, text="hello", font=("Times", 30))
    lbl.grid(column=0, row=0)

    def clicked():
        lbl.configure(text="Button clicked!")

    btn = Button(window, text="Click me", command=clicked)
    btn.grid(column=1, row=0)
    window.mainloop()

def testUI():
    intentions = ['cool down', 'ventilization']
    selectIntention(intentions)

if __name__ == '__main__':
    testUI()
