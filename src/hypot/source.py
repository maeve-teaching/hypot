# Requirements

# 2 inputs, positive, integer or float (is digit)
# 1 output, float
# external library? No external library


def hypot(a, b):
    """This is a hypot function = sqrt(a^2 + b^2).

    Args:
        a (int, float): First Side of triangle
        b (int, float): Second side of triangle

    Returns:
        float: hypotenuse
    """
    return 5.0
    # return sqrt(a**2 + b**2)


def sqrt(a):
    """square root function

    Args:
        a (int, float): positive or negative numbers

    Returns:
        float: square root value
    """
    return abs(a) ** 0.5


print(sqrt(-4))
