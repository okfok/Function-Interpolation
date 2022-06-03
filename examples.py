import numpy as np

import Core


def sqrt():
    return Core.Interpolation(points=[Core.Point(y ** 2, y) for y in range(6)])


def quadratic():
    return Core.Interpolation(points=[Core.Point(x, x ** 2) for x in range(-5, 6)])


def cubic():
    return Core.Interpolation(points=[Core.Point(x, x ** 3) for x in range(-5, 6)])


def sin():
    return Core.Interpolation(
        points=[
            Core.Point(np.pi * x / 180, np.sin(np.pi * x / 180))
            for x in range(-180, 181, 30)]
    )


def cos():
    return Core.Interpolation(
        points=[
            Core.Point(np.pi * x / 180, np.cos(np.pi * x / 180))
            for x in range(-180, 181, 30)]
    )
