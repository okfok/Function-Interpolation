from tkinter.filedialog import askopenfilename, asksaveasfilename

import Core
import config
import examples
from GUI import funcs
from GUI.main import app


# Buttons ------------------------------------------

def add_clicked(event):
    try:
        x, y = funcs.get_x_y()
    except TypeError:
        return
    app.interp.add_point(Core.Point(x, y))
    funcs.display_input_points()


def delete_clicked(event):
    funcs.delete_selected_points()
    funcs.display_input_points()


def clear_clicked(event):
    app.interp.clear_points()
    funcs.display_input_points()


def graph_clicked(event):
    funcs.draw_graph(funcs.get_x0())
    # funcs.display_graph(fig)


def listbox_clicked(event):
    index, *_ = app.pointsListBox.curselection()
    point = app.interp.points[index]
    print(point)
    funcs.set_x_y(point)


# File menu ----------------------------------------

def open_clicked():
    filepath = askopenfilename(
        filetypes=config.INTERPOLATION_FILE_TYPE,
        initialdir=config.INITIAL_DIR,
    )
    if not filepath:
        return
    app.interp.clear_points()
    with open(filepath, "r") as input_file:
        json = input_file.read()
        app.interp = Core.Interpolation.parse_raw(json)
    funcs.display_input_points()


def save_clicked():
    filepath = asksaveasfilename(
        defaultextension=config.INTERPOLATION_FILE_EXTENSION,
        filetypes=config.INTERPOLATION_FILE_TYPE,
        initialdir=config.INITIAL_DIR,
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        json = app.interp.json()
        output_file.write(json)


# Examples -----------------------------------------

def sqrt_example():
    app.interp = examples.sqrt()
    funcs.display_input_points()


def quadratic_example():
    app.interp = examples.quadratic()
    funcs.display_input_points()


def cubic_example():
    app.interp = examples.cubic()
    funcs.display_input_points()


def sin_example():
    app.interp = examples.sin()
    funcs.display_input_points()


def cos_example():
    app.interp = examples.cos()
    funcs.display_input_points()


def rand_example():
    app.interp = examples.rand()
    funcs.display_input_points()
