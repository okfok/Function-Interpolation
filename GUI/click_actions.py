from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

from pydantic import ValidationError

import config
import core
import examples
from GUI import utils
from GUI.app import app


# Buttons ------------------------------------------

def add_clicked():
    point = utils.get_point()
    if point is None:
        return
    try:
        app.interp.add_point(point)
    except ValueError:
        messagebox.showerror("Value error", "List already has point with that X")
        app.update()
        return
    except TypeError:
        messagebox.showwarning("Value error", "You should enter X and Y")
        app.update()
        return

    utils.display_points()


def delete_clicked():
    utils.delete_selected_points()
    utils.display_points()


def clear_clicked():
    app.interp.clear_points()
    utils.display_points()


def graph_clicked():
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
        try:
            app.interp = core.Interpolation.parse_raw(json)
        except ValidationError:
            messagebox.showerror("File error", "File is broken!")
    utils.display_points()


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
    utils.display_points()


def cubic_example():
    app.interp = examples.cubic()
    utils.display_points()


def sin_example():
    app.interp = examples.sin()
    utils.display_points()


def cos_example():
    app.interp = examples.cos()
    utils.display_points()


def rand_example():
    app.interp = examples.rand()
    utils.display_points()
