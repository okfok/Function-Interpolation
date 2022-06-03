from tkinter.filedialog import askopenfilename, asksaveasfilename

import Core
import examples
from GUI import prog, funcs


# Buttons ------------------------------------------

def add_clicked(event):
    try:
        x, y = funcs.get_x_y()
    except TypeError:
        return
    prog.interp.add_point(Core.Point(x, y))
    funcs.display_input_points()


def delete_clicked(event):
    funcs.delete_selected_points()
    funcs.display_input_points()


def clear_clicked(event):
    prog.interp.clear_points()
    funcs.display_input_points()


def graph_clicked(event):
    funcs.draw_graph(funcs.get_x0())
    # funcs.display_graph(fig)


def listbox_clicked(event):
    index, *_ = prog.pointsListBox.curselection()
    point = prog.interp.points[index]
    print(point)
    funcs.set_x_y(point)


# File menu ----------------------------------------

def open_clicked():
    filepath = askopenfilename(
        filetypes=[("Interpolation files", "*.interp"), ("All files", "*.*")],
        initialdir='~/',
    )
    if not filepath:
        return
    prog.interp.clear_points()
    with open(filepath, "r") as input_file:
        json = input_file.read()
        prog.interp = Core.Interpolation.parse_raw(json)
    funcs.display_input_points()


def save_clicked():
    filepath = asksaveasfilename(
        defaultextension=".interp",
        filetypes=[("Interpolation files", "*.interp"), ("All files", "*.*")],
        initialdir='~/',
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        json = prog.interp.json()
        output_file.write(json)


def quit_clicked():
    prog.window.quit()
    prog.window.destroy()


# Examples -----------------------------------------

def sqrt_example():
    prog.interp = examples.sqrt()
    funcs.display_input_points()


def quadratic_example():
    prog.interp = examples.quadratic()
    funcs.display_input_points()


def cubic_example():
    prog.interp = examples.cubic()
    funcs.display_input_points()


def sin_example():
    prog.interp = examples.sin()
    funcs.display_input_points()


def cos_example():
    prog.interp = examples.cos()
    funcs.display_input_points()
