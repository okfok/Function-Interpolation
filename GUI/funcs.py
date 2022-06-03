import tkinter as tk

import Core
from GUI import prog


def set_x_y(point: Core.Point) -> None:
    prog.entryX.delete(0, tk.END)
    prog.entryY.delete(0, tk.END)
    prog.entryX.insert(0, str(point.x))
    prog.entryY.insert(0, str(point.y))


def get_x_y() -> tuple:
    x, y = None, None
    try:
        x = float(prog.entryX.get())
        y = float(prog.entryY.get())
    except ValueError:
        pass
    prog.entryX.delete(0, tk.END)
    prog.entryY.delete(0, tk.END)
    return (x, y) if None not in (x, y) else None


def get_x0():
    try:
        x0 = float(prog.entryX0.get())
        return x0 if prog.interp.x_validate(x0) else None
    except ValueError:
        return


def delete_selected_points() -> None:
    for index in reversed(prog.pointsListBox.curselection()):
        prog.interp.delete_point(index)


def display_input_points():
    prog.pointsListBox.delete(0, tk.END)
    for text in map(str, prog.interp.points):
        prog.pointsListBox.insert(tk.END, text)


def display_result(x: float, ly: float, ny: float):
    prog.labelResult['text'] = \
        'Result:\n' + \
        (f'Linear ({x}, {ly})\n'
         if prog.checkbox_linear.get() and ly is not None
         else 'Linear -\n') + \
        (f'Newton ({x}, {ny})'
         if prog.checkbox_newton.get() and ny is not None
         else 'Newton -')


def draw_graph(x0: float = None):
    prog.figure.clear()
    subplot = prog.figure.add_subplot(111)

    subplot.plot(prog.interp.x, prog.interp.y, '.', color='black')

    if len(prog.interp.points) >= 2:
        interval = prog.interp.get_interval()
        ly = ny = None

        if prog.checkbox_linear.get():
            linear = prog.interp.get_linear_interpolation_func()
            subplot.plot(interval, list(map(linear, interval)), '--', label="linear interpolation")
            if isinstance(x0, float):
                ly = linear(x0)
                subplot.plot(x0, ly, 'o')

        if prog.checkbox_newton.get():
            newton = prog.interp.get_newton_interpolation_func()
            subplot.plot(interval, list(map(newton, interval)), '-.', label="newton interpolation")
            if isinstance(x0, float):
                ny = newton(x0)
                subplot.plot(x0, ny, 'o')

        display_result(x0, ly, ny)

        subplot.legend(loc='best')

    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    subplot.grid(True)

    prog.graph.draw()
    prog.toolbar.update()
