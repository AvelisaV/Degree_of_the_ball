import pytest
from degree_ball import degrees


test_data = [
    (12, 5, 4, 7, 14.6),
    (36, 9, 7, 13, 132.89),
    (17, 4, 9, 6, 10.33)
]


@pytest.mark.parametrize('time, accel, rad, veloc, expected', test_data)
def test_degree_ball(time: float, accel: float, rad: float, veloc: float,
                     expected: float) -> float:
    assert degrees(time, accel, rad, veloc) == expected
