"""
    This file contains the necessary user interface.
"""
from tkinter import *
from tkinter import messagebox

def displayRemedialActions(actions):
    window = Tk()
    window.title('Remedial Actions Selection')
    var = StringVar()
    var.set('')
    lbl = Label(window, text="Would you consider doing this instead:", font=("Times", 20))
    lbl.pack()

    def okayClicked():
        if var.get() == '':
            messagebox.showerror('No Selected','Error! Please select your intention.')
            return
        messagebox.showinfo('Remedial Action Selected', 'We will do ' + var.get().upper() + ' instead. Goodbye!')
        window.destroy()
        return var.get()

    def radioChoice():
        print("You selected " + var.get())

    def cancelClicked():
        window.destroy()

    for option in actions:
        Radiobutton(window, indicatoron=0, width=50, text=option, padx=20, font=("Aerial Bold", 15), variable=var, command=radioChoice,value=option).pack(anchor=CENTER)

    Button(window, text="OKAY", command=okayClicked).pack(side=LEFT, expand=True, fill='both')
    Button(window, text="CANCEL", command=cancelClicked).pack(side=RIGHT, expand=True, fill='both')
    window.mainloop()


def selectIntention(intentions):
    window = Tk()
    window.title('Remedial Actions Intention')
    # window.geometry('350x200')
    var = StringVar()
    var.set('')
    lbl = Label(window, text="Conflicts Detected! Please choose the proper intentions:", font=("Times", 20))
    lbl.pack()

    def okayClicked():
        if var.get() == '':
            messagebox.showerror('No Selected','Error! Please select your intention.')
            return
        window.destroy()
        # TODO: Get the real display instead
        if var.get() == 'cool down':
            displayRemedialActions(samplePossibleRemediation())

    def cancelClicked():
        window.destroy()

    def radioChoice():
        print("You selected " + var.get())

    for option in intentions:
        Radiobutton(window, indicatoron=0, width=50, text=option, padx=20, font=("Aerial Bold", 15), variable=var, command=radioChoice,value=option).pack(anchor=CENTER)

    Button(window, text="OKAY", command=okayClicked).pack(side=LEFT, expand=True, fill='both')
    Button(window, text="CANCEL", command=cancelClicked).pack(side=RIGHT, expand=True, fill='both')
    window.mainloop()

def samplePossibleRemediation():
    return ['turn on AC']

def testUI():
    intentions = ['cool down', 'ventilization']
    selectIntention(intentions)

if __name__ == '__main__':
    testUI()
