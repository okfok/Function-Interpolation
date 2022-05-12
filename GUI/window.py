import tkinter as tk

window = tk.Tk()
window.title("Interpolation Kursach")

mainframe = tk.Frame(master=window)
frameInput = tk.Frame(master=mainframe)
framePoints = tk.Frame(master=frameInput, relief=tk.SUNKEN, borderwidth=1)
frameCordMenu = tk.Frame(master=frameInput)
frameCord = tk.Frame(master=frameCordMenu)
frameX = tk.Frame(master=frameCord)
frameY = tk.Frame(master=frameCord)

labelX = tk.Label(text="X", master=frameX)
labelY = tk.Label(text="Y", master=frameY)

entryX = tk.Entry(master=frameX, width=10)
entryY = tk.Entry(master=frameY, width=10)

button_add = tk.Button(frameCordMenu, text='Add')
button_remove = tk.Button(frameCordMenu, text='Remove')
button_clear = tk.Button(frameCordMenu, text='Clear')
button_open = tk.Button(frameInput, text="Open")
button_save = tk.Button(frameInput, text="Save")

labelPoints = tk.Label(text='', master=framePoints, width=20)






