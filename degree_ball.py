from math import pi


def degrees(time: float, accel: float, rad: float, veloc: float = 0) -> float:
    """Calculate degree of the ball based on elapsed time,
     acceleration, radius and velocity.

    Args:
        time: float - elapsed time.
        accel: float - acceleration of the ball during movement.
        rad: float - radius of the ball.
        veloc: float - velocity of the ball during movement.

    Returns:
        float
    """

    circle = 2 * pi * rad
    square = veloc + (accel * (time) ** 2 / 2)
    degree = (square / circle).__round__(2)

    return degree


print(degrees(17, 4, 9, 6))
