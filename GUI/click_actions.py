import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import matplotlib.pyplot as plt
from PIL import ImageTk, Image

import Core
import GUI.window as w
import config


def display_input_points():
    w.labelPoints['text'] = str(Core.interp)


def graph_display(img_path):
    img = Image.open(img_path)
    img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    w.graph = tk.Label(w.frameOutput, image=img)
    w.graph.image = img
    w.graph.grid(row=1, column=0, sticky="ew", padx=5)


def display_result(x: float, ly: float, ny: float):
    w.labelResult['text'] = f'Result:\nlinear X0({x}, {ly})\nnewton X0({x}, {ny})'


def draw_graph(x0: float = None):
    interp = Core.interp

    plt.plot(interp.x, interp.y, '.', color='black')

    if len(interp.points) >= 2:
        linear = interp.get_linear_interpolation_func()
        newton = interp.get_newton_interpolation_func()

        interval = interp.get_interval()

        plt.plot(interval, linear(interval), '--', label="linear interpolation")
        plt.plot(interval, newton(interval), '--', label="newton interpolation")

        if isinstance(x0, float):
            x = x0
            ly = linear(x0)
            ny = newton(x0)
            plt.plot(x, ly, 'o')
            plt.plot(x, ny, 'o')
            display_result(x, ly, ny)

        plt.legend(loc='best')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig(config.GRAPH_FILE_PATH)
    plt.close()


def add_clicked(event):
    x = float(w.entryX.get())
    y = float(w.entryY.get())
    Core.interp.add_point(Core.Point(x, y))
    display_input_points()


def remove_clicked(event):
    x = float(w.entryX.get())
    y = float(w.entryY.get())
    Core.interp.remove_point(Core.Point(x, y))
    display_input_points()


def clear_clicked(event):
    Core.interp.clear_points()
    display_input_points()


def graph_clicked(event):
    try:
        x0 = float(w.entryX0.get())
    except:
        x0 = None
    draw_graph(x0)
    graph_display(config.GRAPH_FILE_PATH)


def open_clicked():
    filepath = askopenfilename(
        filetypes=[("Interpolation files", "*.interp"), ("All files", "*.*")]
    )
    if not filepath:
        return
    Core.interp.clear_points()
    with open(filepath, "r") as input_file:
        text = input_file.read()
        Core.interp = Core.Interpolation.parse_raw(text)
    display_input_points()
    # w.window.title(f"Простой текстовый редактор - {filepath}")


def save_clicked():
    filepath = asksaveasfilename(
        defaultextension=".interp",
        filetypes=[("Interpolation files", "*.interp"), ("All files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = Core.interp.json()
        output_file.write(text)
    # w.window.title(f"Простой текстовый редактор - {filepath}")
