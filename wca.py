import numpy


class Heading:
    def __init__(self, course):
        self._course = course

    @property
    def value(self):
        return self._course

    @property
    def radians(self):
        return numpy.radians(-self._course)

    def vector(self, radius) -> (float, float):
        return radius * numpy.cos(self.radians), radius * numpy.sin(self.radians)

    def __float__(self):
        return self.value


def solve(
        wind_dir: Heading,
        wind_speed: float,
        true_course: Heading,
        true_airspeed: float
) -> (float, float):
    cc, cs = true_course.vector(1)
    wx, wy = wind_dir.vector(-wind_speed)

    csw = cc * wx + cs * wy
    t = csw + numpy.sqrt(csw ** 2 - wind_speed ** 2 + true_airspeed ** 2)
    ground_speed = t
    ground_x, ground_y = true_course.vector(t)
    heading = -numpy.degrees(numpy.arctan2(ground_y - wy, ground_x - wx))
    wind_correction_angle = heading - true_course.value
    return ground_speed, wind_correction_angle
