from tkinter import *


class CanvasUsine(Canvas):
    selected = None
    last_xy = None

    def bind_item(self):
        self.tag_bind('copy_and_drop', "<ButtonPress-1>", self.on_item_click_copy)
        self.tag_bind('copy_and_drop', "<Button1-Motion>", lambda e: self._move_selected(e.x, e.y))
        self.tag_bind('copy_and_drop', "<ButtonRelease-1>", lambda e: self._move_selected(e.x, e.y, 0))

        self.tag_bind('resizeable', "<ButtonPress-3>", self.on_item_click)
        #  self.tag_bind('resizeable', "<Button3-Motion>", lambda e: self._resize_item(e.x, e.y))
        self.tag_bind('resizeable', "<ButtonRelease-3>", lambda e: self._resize_item(e.x, e.y))

        self.tag_bind('move_and_drop', "<ButtonPress-1>", self.on_item_click)
        self.tag_bind('move_and_drop', "<Button1-Motion>", lambda e: self._move_item(e.x, e.y, 5))
        self.tag_bind('move_and_drop', "<ButtonRelease-1>", lambda e: self._move_item(e.x, e.y))

    def _move_selected(self, x1, y1, min_pixels=5):
        x0, y0 = self.last_xy
        dx, dy = x1 - x0, y1 - y0
        if abs(dx) > min_pixels or abs(dy) > min_pixels:
            self.move(self.selected, dx, dy)
            self.last_xy = x1, y1

    def _resize_item(self, xe, ye):
        x0, y0, x1, y1 = self.coords('current')
        print(x0, y0, x1, y1, "\tevent ", xe, ye, "\tlast", self.last_xy)
        x1 += (xe - self.last_xy[0])
        y1 += (ye - self.last_xy[1])
        print(x0, y0, x1, y1, "\tevent ", xe, ye, "\tlast", self.last_xy)
        self.coords('current', x0, y0, x1, y1)

    def on_item_click(self, event):
        self.last_xy = event.x, event.y

    def on_item_click_copy(self, event):
        self.on_item_click(event)
        self._copy_curent()

    def _copy_curent(self):
        iid = self.find_withtag('current')
        self.selected = self._copy_item(iid)

    def _move_item(self, x1, y1, mini=0):
        if abs(self.last_xy[0]-x1 + self.last_xy[1]-y1) > mini:
            coords = list(self.coords('current'))
            coords[0] += x1 - self.last_xy[0]
            coords[2] += x1 - self.last_xy[0]
            coords[1] += y1 - self.last_xy[1]
            coords[3] += y1 - self.last_xy[1]
            self.coords('current', *coords)
            self.last_xy = x1,y1

    def _copy_item(self, iid):
        # type_ = self.type(iid)
        # assert type_ == 'oval'
        coords = self.coords(iid)
        kwds = self.itemconfigure(iid)
        kwds = {k: v[-1] for k, v in kwds.items()}
        return self.create_oval(*coords, **kwds)


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window, bg='white')
        window.title("Changement de couleur")
        self.pack()

        self.canvas = CanvasUsine(self, height=600, width=800)
        self.canvas.pack()

        self.canvas.create_rectangle(10, 10, 100, 200, activefill="blue", fill="green", tags='copy_and_drop')
        self.canvas.create_rectangle(10,210, 100, 400, activefill="blue", fill="green", tags=('resizeable',
                                                                                              'move_and_drop'))
        self.canvas.bind_item()
        print(self.canvas.__dict__)


root = Tk()
test = Test(root)
test.mainloop()
