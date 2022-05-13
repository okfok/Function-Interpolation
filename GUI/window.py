import tkinter as tk

from PIL import ImageTk, Image

window = tk.Tk()
window.title("Interpolation Kursach")

frameMenu = tk.Frame(window, relief=tk.RAISED, bd=2)
frameInput = tk.Frame(frameMenu)

labelX = tk.Label(frameInput, text="X")
labelY = tk.Label(frameInput, text="Y")
labelX0 = tk.Label(frameInput, text="X0")

entryX = tk.Entry(frameInput, width=10)
entryY = tk.Entry(frameInput, width=10)
entryX0 = tk.Entry(frameInput, width=10)

button_add = tk.Button(frameInput, text='Add')
button_remove = tk.Button(frameInput, text='Remove')
button_clear = tk.Button(frameInput, text='Clear')
button_open = tk.Button(frameInput, text="Open")
button_save = tk.Button(frameInput, text="Save")
button_graph = tk.Button(frameInput, text="Graph")

labelPoints = tk.Label(frameMenu, text='', width=20, height=25, bg='white')

frameOutput = tk.Frame(window)

labelResult = tk.Label(frameOutput, text="Result:\n(2, 4)", bg='white')
graph = tk.Canvas(frameOutput, width=800, height=600)
