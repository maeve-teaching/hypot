import pytest
import hypot.source as source


# test sqrt function for input is even
def test_sqrt_even():
    input = 4
    e_output = 2.0
    output = source.sqrt(input)
    assert output == e_output

# test sqrt scenario for input is odd
def test_sqrt_odd():
    input = 9
    e_output = 3.0
    output = source.sqrt(input)
    assert output == e_output

# test negative
def test_sqrt_negative():
    input = -9
    e_output = 3.0
    output = source.sqrt(input)
    assert output == e_output
# test hypot function