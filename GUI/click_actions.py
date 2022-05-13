import tkinter as tk

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


def draw_graph(x0: float = None):
    interp = Core.interp

    plt.plot(interp.x, interp.y, '.', color='black')

    if len(interp.points) >= 2:
        linear = interp.get_linear_interpolation_func()
        newton = interp.get_newton_interpolation_func()

        interval = interp.get_interval()

        plt.plot(interval, linear(interval), '--', label="linear interpolation")
        plt.plot(interval, newton(interval), '--', label="newton interpolation")

        if x0 is not None:
            plt.plot(x0, linear(x0), 'o', lable='X0 linear')
            plt.plot(x0, newton(x0), 'o', lable='X0 newton')

        plt.legend(loc=1)

    plt.xlabel('x')
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
    draw_graph()
    graph_display(config.GRAPH_FILE_PATH)

# def open_file():
#     """Открываем файл для редактирования"""
#     filepath = askopenfilename(
#         filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete("1.0", tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Простой текстовый редактор - {filepath}")
#
#
# def save_file():
#     """Сохраняем текущий файл как новый файл."""
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get("1.0", tk.END)
#         output_file.write(text)
#     window.title(f"Простой текстовый редактор - {filepath}")
