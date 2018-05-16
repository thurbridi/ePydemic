import pytest
from epydemic import Lattice

xfail = pytest.xfail


def test_setitem():
    height = 3
    width = 3
    l = Lattice(height=height, width=width)

    v = 1
    for i in range(0, height):
        for j in range(0, width):
            l[i, j] = v
            v += 1

    assert l.grid[0, 0] == 1
    assert l.grid[0, 1] == 2
    assert l.grid[0, 2] == 3

    assert l.grid[1, 0] == 4
    assert l.grid[1, 1] == 5
    assert l.grid[1, 2] == 6

    assert l.grid[2, 0] == 7
    assert l.grid[2, 1] == 8
    assert l.grid[2, 2] == 9


def test_getitem():
    height = 3
    width = 3
    l = Lattice(height=height, width=width)

    v = 1
    for i in range(0, height):
        for j in range(0, width):
            l.grid[i, j] = v
            v += 1

    assert l[0, 0] == 1
    assert l[0, 1] == 2
    assert l[0, 2] == 3
    assert l[1, 0] == 4
    assert l[1, 1] == 5
    assert l[1, 2] == 6
    assert l[2, 0] == 7
    assert l[2, 1] == 8
    assert l[2, 2] == 9


def test_borders():
    height = 3
    width = 3
    l = Lattice(height=height, width=width)

    v = 1
    for i in range(0, height):
        for j in range(0, width):
            l.grid[i, j] = v
            v += 1

    """
    9 7 8 9 7
    3 1 2 3 1
    6 4 5 6 4
    9 7 8 9 7
    3 1 2 3 1
    """

    assert l[-1, 0] == 7
    assert l[-1, 1] == 8
    assert l[-1, 2] == 9
    assert l[3, 0] == 1
    assert l[3, 1] == 2
    assert l[3, 2] == 3
    assert l[0, -1] == 3
    assert l[1, -1] == 6
    assert l[2, -1] == 9
    assert l[0, 3] == 1
    assert l[1, 3] == 4
    assert l[2, 3] == 7
    assert l[-1, -1] == 9
    assert l[-1, 3] == 7
    assert l[3, -1] == 3
    assert l[3, 3] == 1
