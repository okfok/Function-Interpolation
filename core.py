from typing import Callable

import numpy as np
from pydantic import BaseModel, Field

import config


class Point(BaseModel):
    x: float
    y: float

    def __lt__(self, other: 'Point'):
        return self.x < other.x

    def __str__(self):
        return f'({round(self.x, 5)}, {round(self.y, 5)})'

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)

    def __init__(self, x: float, y: float):
        super(Point, self).__init__(x=x, y=y)


class Interpolation(BaseModel):
    points: list[Point] = Field(default_factory=list)

    def __str__(self):
        return '\n'.join([str(point) for point in self.points])

    @property
    def x(self) -> np.ndarray:
        return np.array([point.x for point in self.points])

    @property
    def y(self) -> np.ndarray:
        return np.array([point.y for point in self.points])

    @property
    def min_x(self) -> float:
        return self.points[0].x

    @property
    def max_x(self) -> float:
        return self.points[-1].x

    def sort_points(self) -> None:
        self.points.sort()

    def add_point(self, point: Point) -> None:
        if not isinstance(point, Point) or any(point.x == p.x for p in self.points):
            raise ValueError("List already has point with that X")
        else:
            self.points.append(point)
            self.sort_points()

    def remove_point(self, point: Point) -> None:
        if point in self.points:
            self.points.remove(point)

    def del_point(self, index: int) -> None:
        if 0 <= index <= len(self.points):
            self.points.pop(index)

    def clear_points(self) -> None:
        self.points.clear()

    def x_validate(self, x) -> bool:
        if isinstance(x, float):
            return self.min_x <= x <= self.max_x
        else:
            return False

    def get_interval(self) -> np.ndarray:
        self.sort_points()
        return np.linspace(
            self.min_x, self.max_x,
            len(self.points) * config.GRAPH_ACCURACY
        )

    def linear_interpolation_func(self, x0: float) -> float:
        for i in range(len(self.points) - 1):
            if self.points[i].x <= x0 <= self.points[i + 1].x:
                return (self.points[i + 1].y - self.points[i].y) * (x0 - self.points[i].x) \
                       / (self.points[i + 1].x - self.points[i].x) + self.points[i].y

    def get_newton_interpolation_func(self) -> Callable:
        def get_quotients_table(x, y):
            quotients = [[0] * len(x) for _ in range(len(x))]

            for i in range(len(x)):
                quotients[i][0] = y[i]

            for i in range(1, len(x)):
                for j in range(i, len(x)):
                    quotients[j][i] = (quotients[j][i - 1] - quotients[j - 1][i - 1]) / (x[j] - x[j - i])

            return quotients

        def get_quot_diag(quotients):
            diag = []
            for i in range(len(quotients)):
                diag.append(quotients[i][i])
            return diag

        quot_diag = get_quot_diag(get_quotients_table(self.x, self.y))

        def newton_interpolation_func(x0: float):
            result = quot_diag[0]
            for i in range(1, len(quot_diag)):
                p = quot_diag[i]
                for j in range(i):
                    p *= (x0 - self.x[j])
                result += p
            return result

        return newton_interpolation_func
