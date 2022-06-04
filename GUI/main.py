import tkinter as tk

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import Core


class Checkbutton(tk.Checkbutton):

    def __init__(self, master, **kwargs):
        self.var = tk.BooleanVar()
        self.var.set(True)
        super(Checkbutton, self).__init__(
            master,
            **kwargs,
            variable=self.var,
            onvalue=1,
            offvalue=0
        )

    def get(self):
        return self.var.get()


class App:
    def __init__(self):
        self.interp = Core.Interpolation()

        self._root = tk.Tk()
        self._root.resizable(False, False)
        self._root.title("Interpolation Kursach")

        self.menu = tk.Menu(self._root)
        self._root.config(menu=self.menu)

        self.menu_file = tk.Menu(self.menu, tearoff=0)
        self.menu_examples = tk.Menu(self.menu, tearoff=0)

        self.frame_menu = tk.Frame(self._root, relief=tk.RAISED, bd=2)
        self.frame_input = tk.Frame(self.frame_menu)

        self.labelX = tk.Label(self.frame_input, text="X")
        self.labelY = tk.Label(self.frame_input, text="Y")
        self.labelX0 = tk.Label(self.frame_input, text="X0")

        self.entryX = tk.Entry(self.frame_input, width=10)
        self.entryY = tk.Entry(self.frame_input, width=10)
        self.entryX0 = tk.Entry(self.frame_input, width=10)

        self.button_add = tk.Button(self.frame_input, text='Add')
        self.button_delete = tk.Button(self.frame_input, text='Delete')
        self.button_clear = tk.Button(self.frame_input, text='Clear')
        self.button_graph = tk.Button(self.frame_input, text="Graph")

        self.checkbox_linear = Checkbutton(self.frame_input, text="Linear")
        self.checkbox_newton = Checkbutton(self.frame_input, text="Newton")

        self.scrollbar = tk.Scrollbar(self.frame_menu)

        self.listbox_points = tk.Listbox(
            self.scrollbar,
            selectmode=tk.EXTENDED,
            width=30,
            height=30,
            bg='white',
        )

        self.frame_output = tk.Frame(self._root, bg='white')

        self.label_result = tk.Label(
            self.frame_output,
            text="Result:\nLinear -\nNewton -",
            bg='white'
        )

        self.figure = Figure()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame_output)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame_output)

    def mainloop(self):
        self._root.mainloop()

    def exit(self):
        self._root.quit()
        self._root.destroy()


app = App()
