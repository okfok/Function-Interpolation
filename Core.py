from typing import Callable

import numpy as np
from pydantic import BaseModel, Field
from scipy import interpolate

import config


class Point(BaseModel):
    x: float
    y: float

    def __lt__(self, other: 'Point'):
        return self.x < other.x

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __init__(self, x: float, y: float):
        super(Point, self).__init__(x=x, y=y)


class Interpolation(BaseModel):
    points: list[Point] = Field(default_factory=list)

    def add_point(self, point: Point) -> None:
        if point not in self.points:
            self.points.append(point)
            self.points.sort()

    def remove_point(self, point: Point) -> None:
        if point in self.points:
            self.points.remove(point)

    def clear_points(self) -> None:
        self.points.clear()

    @property
    def x(self) -> np.ndarray:
        return np.array([point.x for point in self.points])

    @property
    def y(self) -> np.ndarray:
        return np.array([point.y for point in self.points])

    def get_interval(self):
        self.points.sort()
        min_ = self.points[0].x
        max_ = self.points[-1].x
        return np.linspace(min_, max_, int((max_ - min_) * config.GRAPH_ACCURACY))

    def get_linear_interpolation_func(self) -> Callable:
        return interpolate.interp1d(self.x, self.y)

    def get_newton_interpolation_func(self) -> Callable:
        def table(x, y):
            quotients = [[0] * len(x) for _ in range(len(x))]

            for i in range(len(x)):
                quotients[i][0] = y[i]

            for i in range(1, len(x)):
                for j in range(i, len(x)):
                    quotients[j][i] = (quotients[j][i - 1] - quotients[j - 1][i - 1]) / (x[j] - x[j - i])

            return quotients

        def get_corner(quotients):
            link = []
            for i in range(len(quotients)):
                link.append(quotients[i][i])
            return link

        quotients_table = table(self.x, self.y)
        corners = get_corner(quotients_table)

        def newton_func(x_p):
            result = corners[0]
            for i in range(1, len(corners)):
                p = corners[i]
                for j in range(i):
                    p *= (x_p - self.x[j])
                result += p
            return result

        return newton_func

    def __str__(self):
        return '\n'.join([str(point) for point in self.points])


interp = Interpolation()
