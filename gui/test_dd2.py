from tkinter import *


class Canvas_Usine(Canvas):
    selected = None
    last_xy = None

    def bind_item(self):
        self.tag_bind('copy_and_drop', "<ButtonPress-1>", self.on_item_click)
        self.tag_bind('copy_and_drop', "<Button1-Motion>",
                      lambda e: self._move_selected(e.x, e.y))
        self.tag_bind('copy_and_drop', "<ButtonRelease-1>",
                      lambda e: self._move_selected(e.x, e.y, 0))

    def _move_selected(self, x1, y1, min_pixels=5):
        x0, y0 = self.last_xy
        dx, dy = x1 - x0, y1 - y0
        if abs(dx) > min_pixels or abs(dy) > min_pixels:
            self.move(self.selected, dx, dy)
            self.last_xy = x1, y1

    def _resize_item(self, e):
        self.last_xy = e.x, e.y
        x0, y0, x1, y1 = self.coords('current')
        x1 += x1-self.last_xy[0]
        x1 += y1 - self.last_xy[1]
        self.coords('current', x0, y0, x1, y1)

    def on_item_click(self, event):
        iid = self.find_withtag('current')
        self.selected = self._copy_item(iid)
        print("event", event)
        self.last_xy = event.x, event.y

    def _copy_item(self, iid):
        # type_ = self.type(iid)
        # assert type_ == 'oval'
        coords = self.coords(iid)
        print(iid)
        print("test", self.__dict__)
        kwds = self.itemconfigure(iid)
        kwds = {k: v[-1] for k, v in kwds.items()}
        return self.create_oval(*coords, **kwds)


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window, bg='white')
        window.title("Changement de couleur")
        self.pack()

        self.canvas = Canvas_Usine(self, height=800, width=600)
        self.canvas.pack()

        self.canvas.create_rectangle(10, 10, 100, 200, activefill="blue", fill="green", tags='copy_and_drop')
        self.canvas.create_rectangle(10,210, 100, 400, activefill="blue", fill="green", tags='resizeable')
        self.canvas.bind_item()
        print(self.canvas.__dict__)


root = Tk()
test = Test(root)
test.mainloop()
