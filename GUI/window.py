import tkinter as tk

window = tk.Tk()
window.title("Interpolation Kursach")

menu = tk.Menu(window)
menu_file = tk.Menu(menu, tearoff=0)

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
button_graph = tk.Button(frameInput, text="Graph")

labelPoints = tk.Label(
    frameMenu,
    text='',
    width=20,
    height=28,
    bg='white',
    relief=tk.SUNKEN
)

frameOutput = tk.Frame(window)

labelResult = tk.Label(frameOutput, text="Result:\n", bg='white')
graph = tk.Canvas(frameOutput, width=800, height=600)
