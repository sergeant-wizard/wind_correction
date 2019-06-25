import wca

import numpy


def test_solve() -> None:
    wind_dir = wca.Heading(30)
    wind_speed = 16
    true_course = wca.Heading(299)
    true_airspeed = 100
    ground_speed, wind_correction_angle = wca.solve(wind_dir, wind_speed, true_course, true_airspeed)

    heading = wca.Heading(true_course.value + wind_correction_angle)
    gx, gy = true_course.vector(ground_speed)
    wx, wy = wind_dir.vector(-wind_speed)
    tx, ty = heading.vector(true_airspeed)
    assert numpy.isclose(tx + wx, gx)
    assert numpy.isclose(ty + wy, gy)
