from tkinter import *


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window, bg='red', width=70000)
        window.grid_propagate(0)
        window.title("Message cadré")
        self.pack()

        self.message = Message(self, text="coucou", width=30000, justify="left")
        self.message.pack()


root = Tk()
test = Test(root)
test.mainloop()