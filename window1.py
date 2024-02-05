from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) -> object:
        self.label1 = Label(self, text="Welcome" )
        self.label1.grid(row=0, column=0, sticky=W)


window = Tk()
window.title("This is a test window")
window.geometry("300x100")
app = Application(window)
app.mainloop()