from tkinter.filedialog import askopenfilename, asksaveasfilename

import config
import core
import examples
from GUI import utils
from GUI.app import app


# Buttons ------------------------------------------

def add_clicked(event):
    try:
        x, y = utils.get_x_y()
    except TypeError:
        return
    app.interp.add_point(core.Point(x, y))
    utils.display_input_points()


def delete_clicked(event):
    utils.delete_selected_points()
    utils.display_input_points()


def clear_clicked(event):
    app.interp.clear_points()
    utils.display_input_points()


def graph_clicked(event):
    utils.draw_graph(utils.get_x0())


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
        app.interp = core.Interpolation.parse_raw(json)
    utils.display_input_points()


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


# Examples menu-------------------------------------

def quadratic_example():
    app.interp = examples.quadratic()
    utils.display_input_points()


def cubic_example():
    app.interp = examples.cubic()
    utils.display_input_points()


def sin_example():
    app.interp = examples.sin()
    utils.display_input_points()


def cos_example():
    app.interp = examples.cos()
    utils.display_input_points()


def rand_example():
    app.interp = examples.rand()
    utils.display_input_points()
