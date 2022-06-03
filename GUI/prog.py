import tkinter as tk

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import Core

interp = Core.Interpolation()

window = tk.Tk()
window.resizable(False, False)
window.title("Interpolation Kursach")

menu = tk.Menu(window)
menu_file = tk.Menu(menu, tearoff=0)
menu_examples = tk.Menu(menu, tearoff=0)

frameMenu = tk.Frame(window, relief=tk.RAISED, bd=2)
frameInput = tk.Frame(frameMenu)

labelX = tk.Label(frameInput, text="X")
labelY = tk.Label(frameInput, text="Y")
labelX0 = tk.Label(frameInput, text="X0")

entryX = tk.Entry(frameInput, width=15)
entryY = tk.Entry(frameInput, width=15)
entryX0 = tk.Entry(frameInput, width=15)

button_add = tk.Button(frameInput, text='Add')
button_delete = tk.Button(frameInput, text='Delete')
button_clear = tk.Button(frameInput, text='Clear')
button_graph = tk.Button(frameInput, text="Graph")

scrollbar = tk.Scrollbar(frameMenu)

pointsListBox = tk.Listbox(
    scrollbar,
    selectmode=tk.EXTENDED,
    width=45,
    height=30,
    bg='white',
    relief=tk.SUNKEN
)

frameOutput = tk.Frame(window, bg='white')

labelResult = tk.Label(frameOutput, text="Result:\nLinear X0()\nNewton X0()", bg='white')

figure = Figure()
graph = FigureCanvasTkAgg(figure, master=frameOutput)
toolbar = NavigationToolbar2Tk(graph, frameOutput)
