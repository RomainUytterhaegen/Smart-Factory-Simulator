from tkinter import *


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window, bg='red')

        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky='news')

        self.message_textmode = Message(self, text="Coucou", width=100, justify='left',
                                        highlightcolor='blue')
        self.message_textmode.grid(row=0, column=0, padx=20, pady=20, sticky='news')

root = Tk()
test = Test(root)
test.mainloop()