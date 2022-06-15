import tkinter as tk
from tkinter import messagebox

import core
from GUI.app import app


def get_point() -> core.Point:
    try:
        x = float(app.entryX.get())
        y = float(app.entryY.get())
    except ValueError:
        messagebox.showerror("Value error", "X and Y should be numbers!")
        app.update()
        return
    if core.INF in (x, y):
        messagebox.showerror("Value error", "X and Y should be numbers!")
        return
    app.entryX.delete(0, tk.END)
    app.entryY.delete(0, tk.END)
    return core.Point(x, y)


def get_x0():
    x0 = app.entryX0.get()
    if x0 == '':
        return
    try:
        x0 = float(x0)
        if app.interp.x_validate(x0):
            return x0
        else:
            messagebox.showerror("Value error", "X0 is out of interpolation range!")
    except ValueError:
        messagebox.showerror("Value error", "X0 should be number!")


def delete_selected_points() -> None:
    for index in reversed(app.listbox_points.curselection()):
        app.interp.del_point(index)


def display_points():
    app.listbox_points.delete(0, tk.END)
    for text in map(str, app.interp.points):
        app.listbox_points.insert(tk.END, text)


def display_result(x: float, ly: float, ny: float):
    app.label_result['text'] = \
        'Result:\n' + \
        (f'Linear ({round(x, 5)}, {round(ly, 5)})\n'
         if app.checkbox_linear.get() and ly is not None
         else 'Linear -\n') + \
        (f'Newton ({round(x, 5)}, {round(ny, 5)})'
         if app.checkbox_newton.get() and ny is not None
         else 'Newton -')


def draw_graph(x0: float = None):
    app.figure.clear()
    ax = app.figure.add_subplot(111)

    ax.plot(app.interp.x, app.interp.y, '.', label="input points", color='black')
    ly = ny = None
    interval = app.interp.get_interval()

    if app.checkbox_linear.get() and len(app.interp.points) >= 2:
        linear = app.interp.linear_interpolation_func
        ax.plot(
            interval,
            list(map(linear, interval)),
            '--',
            label="linear interpolation",
            color='blue'
        )
        if isinstance(x0, float):
            ly = linear(x0)
            ax.plot(x0, ly, 'o', color='blue')

    if app.checkbox_newton.get() and len(app.interp.points) >= 3:
        newton = app.interp.get_newton_interpolation_func()
        y = list(map(newton, interval))
        ax.plot(
            interval,
            y, '-.',
            label="newton interpolation",
            color='green'
        )
        if isinstance(x0, float):
            ny = newton(x0)
            ax.plot(x0, ny, 'o', color='green')

    display_result(x0, ly, ny)

    ax.legend(loc='best')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

    app.canvas.draw()
    app.toolbar.update()

    match len(app.interp.points):
        case l if l < 2:
            messagebox.showerror("Value error", "Not enough points!\nShould be 2 or more")
        case 2:
            messagebox.showwarning("Warning", "You enter 2 point.\nNewton interpolation is similar to linear")
        case _:
            pass
