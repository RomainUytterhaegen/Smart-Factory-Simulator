from tkinter import *


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window, bg='white')
        window.title("Changement de couleur")
        self.pack()

        self.bouton1 = Button(self, text='Rouge', command=self.changer_fond)
        self.bouton1.pack()

    def changer_fond(self):
        print("test", file=sys.stderr)
        self.bg ='Rouge'


root = Tk()
test = Test(root)
test.mainloop()
