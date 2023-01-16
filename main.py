from tkinter import *
from tkinter import ttk as tkk

# conversion tables I made to translate between QWERTY and Dvorak
from conversion_tables import qtd, dtq

class Converter:
    def __init__(self, master):
        self.master = master

        self.master.title("Layout Converter")
        self.master.geometry("600x200")
        self.master.resizable(False, False)

        self.input = Entry(self.master, width=100)
        self.result = Entry(self.master, width=100)
        self.selection = tkk.Combobox(self.master)

        self.input.bind("<KeyRelease>", self.convert)
        self.selection.bind("<<ComboboxSelected>>", self.convert)

        self.input.grid(row=0)
        self.result.grid(row=1)
        self.selection.grid(row=3)

        self.result.configure(state='readonly')
        self.selection.configure(state='readonly')

        self.selection['values'] = ("QWERTY to Dvorak", "Dvorak to QWERTY")

        self.selection.current(0)


    # convert text between QWERTY & Dvorak using conversion tables
    def convert(self, event):
        table = qtd if self.selection.get() == "QWERTY to Dvorak" else dtq
        text = self.input.get()
        text = "".join(table.get(c, c) for c in text)
        self.result.configure(state='normal')
        self.result.delete(0, END)
        self.result.insert(0, text)
        self.result.configure(state='readonly')

if __name__ == "__main__":
    root = Tk()
    Converter = Converter(root)
    root.mainloop()

# still lots of room for improvement
# could convert to a canvas and style it so that it isn't width constrained