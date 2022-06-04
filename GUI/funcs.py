import tkinter as tk

import Core
from GUI.main import app


def set_x_y(point: Core.Point) -> None:
    app.entryX.delete(0, tk.END)
    app.entryY.delete(0, tk.END)
    app.entryX.insert(0, str(point.x))
    app.entryY.insert(0, str(point.y))


def get_x_y() -> tuple:
    x, y = None, None
    try:
        x = float(app.entryX.get())
        y = float(app.entryY.get())
    except ValueError:
        pass
    app.entryX.delete(0, tk.END)
    app.entryY.delete(0, tk.END)
    return (x, y) if None not in (x, y) else None


def get_x0():
    try:
        x0 = float(app.entryX0.get())
        return x0 if app.interp.x_validate(x0) else None
    except ValueError:
        return


def delete_selected_points() -> None:
    for index in reversed(app.pointsListBox.curselection()):
        app.interp.delete_point(index)


def display_input_points():
    app.pointsListBox.delete(0, tk.END)
    for text in map(str, app.interp.points):
        app.pointsListBox.insert(tk.END, text)


def display_result(x: float, ly: float, ny: float):
    app.labelResult['text'] = \
        'Result:\n' + \
        (f'Linear ({round(x, 5)}, {round(ly, 5)})\n'
         if app.checkbox_linear.get() and ly is not None
         else 'Linear -\n') + \
        (f'Newton ({round(x, 5)}, {round(ny, 5)})'
         if app.checkbox_newton.get() and ny is not None
         else 'Newton -')


def draw_graph(x0: float = None):
    app.figure.clear()
    subplot = app.figure.add_subplot(111)

    subplot.plot(app.interp.x, app.interp.y, '.', color='black')

    if len(app.interp.points) >= 2:
        interval = app.interp.get_interval()
        ly = ny = None

        if app.checkbox_linear.get():
            linear = app.interp.get_linear_interpolation_func()
            subplot.plot(
                interval,
                list(map(linear, interval)),
                '--',
                label="linear interpolation",
                color='blue'
            )
            if isinstance(x0, float):
                ly = linear(x0)
                subplot.plot(x0, ly, 'o', color='blue')

        if app.checkbox_newton.get():
            import warnings
            warnings.filterwarnings('error')
            try:
                newton = app.interp.get_newton_interpolation_func()
                y = list(map(newton, interval))
                subplot.plot(
                    interval,
                    y, '-.',
                    label="newton interpolation",
                    color='green'
                )
                if isinstance(x0, float):
                    ny = newton(x0)
                    subplot.plot(x0, ny, 'o', color='green')
            except Warning:
                pass

        display_result(x0, ly, ny)

        subplot.legend(loc='best')

    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    subplot.grid(True)

    app.graph.draw()
    app.toolbar.update()
