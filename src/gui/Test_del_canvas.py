from tkinter import *


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window, bg='white')
        window.title("Changement de couleur")
        self.pack()

        self.canvas = Canvas(self, height=400, width=400)
        self.canvas.create_rectangle(10, 10, 110, 110, fill="blue", tags="rect")
        self.canvas.bind("<Any-x>", self.suppr_rect, '+')
        window.bind("<ButtonPress-1>", lambda e: self.suppr_rect(), '+')

        self.canvas.pack()
        self.bouton1 = Button(self, text='suppr', command=self.suppr_rect)
        self.bouton1.pack()

    def suppr_rect(self):
        print("coucou")
        self.canvas.delete("rect")

root = Tk()
test = Test(root)
test.mainloop()