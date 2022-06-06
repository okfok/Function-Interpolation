from random import randint

import numpy as np

import core


def quadratic():
    return core.Interpolation(points=[core.Point(x, x ** 2) for x in range(-5, 6)])


def cubic():
    return core.Interpolation(points=[core.Point(x, x ** 3) for x in range(-5, 6)])


def sin():
    return core.Interpolation(
        points=[
            core.Point(np.pi * x / 180, np.sin(np.pi * x / 180))
            for x in range(-180, 181, 30)]
    )


def cos():
    return core.Interpolation(
        points=[
            core.Point(np.pi * x / 180, np.cos(np.pi * x / 180))
            for x in range(-180, 181, 30)]
    )


def rand():
    return core.Interpolation(
        points=[
            core.Point(x, randint(-10, 11))
            for x in range(-10, 11)]
    )
