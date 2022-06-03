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

        self.frameMenu = tk.Frame(self._root, relief=tk.RAISED, bd=2)
        self.frameInput = tk.Frame(self.frameMenu)

        self.labelX = tk.Label(self.frameInput, text="X")
        self.labelY = tk.Label(self.frameInput, text="Y")
        self.labelX0 = tk.Label(self.frameInput, text="X0")

        self.entryX = tk.Entry(self.frameInput, width=10)
        self.entryY = tk.Entry(self.frameInput, width=10)
        self.entryX0 = tk.Entry(self.frameInput, width=10)

        self.button_add = tk.Button(self.frameInput, text='Add')
        self.button_delete = tk.Button(self.frameInput, text='Delete')
        self.button_clear = tk.Button(self.frameInput, text='Clear')
        self.button_graph = tk.Button(self.frameInput, text="Graph")

        self.checkbox_linear = Checkbutton(self.frameInput, text="Linear")
        self.checkbox_newton = Checkbutton(self.frameInput, text="Newton")

        self.scrollbar = tk.Scrollbar(self.frameMenu)

        self.pointsListBox = tk.Listbox(
            self.scrollbar,
            selectmode=tk.EXTENDED,
            width=30,
            height=30,
            bg='white',
        )

        self.frameOutput = tk.Frame(self._root, bg='white')

        self.labelResult = tk.Label(
            self.frameOutput,
            text="Result:\nLinear -\nNewton -",
            bg='white'
        )

        self.figure = Figure()
        self.graph = FigureCanvasTkAgg(self.figure, master=self.frameOutput)
        self.toolbar = NavigationToolbar2Tk(self.graph, self.frameOutput)

    def mainloop(self):
        self._root.mainloop()

    def exit(self):
        self._root.quit()
        self._root.destroy()


app = App()
