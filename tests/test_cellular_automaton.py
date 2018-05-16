import pytest
from ePydemic import CellularAutomaton

xfail = pytest.xfail


def test_count_neighbors():
    """
    0 0 1 1
    0 2 0 1
    1 1 0 2
    0 1 2 1
    """

    ca = CellularAutomaton(height=4, width=4)
    ca.lattice[0, 0] = 0
    ca.lattice[0, 1] = 0
    ca.lattice[0, 2] = 1
    ca.lattice[0, 3] = 1
    ca.lattice[1, 0] = 0
    ca.lattice[1, 1] = 2
    ca.lattice[1, 2] = 0
    ca.lattice[1, 3] = 1
    ca.lattice[2, 0] = 1
    ca.lattice[2, 1] = 1
    ca.lattice[2, 2] = 0
    ca.lattice[2, 3] = 2
    ca.lattice[3, 0] = 0
    ca.lattice[3, 1] = 1
    ca.lattice[3, 2] = 2
    ca.lattice[3, 3] = 1

    i_count, s_count, r_count = ca.count_neighbors(1, 1)
    assert i_count == 5
    assert s_count == 3
    assert r_count == 0

    i_count, s_count, r_count = ca.count_neighbors(3, 3)
    assert i_count == 3
    assert s_count == 3
    assert r_count == 2


def test_stats():
    """
    0 0 1 1
    0 2 0 1
    1 1 0 2
    0 1 2 1
    """

    ca = CellularAutomaton(height=4, width=4)
    ca.lattice[0, 0] = 0
    ca.lattice[0, 1] = 0
    ca.lattice[0, 2] = 1
    ca.lattice[0, 3] = 1
    ca.lattice[1, 0] = 0
    ca.lattice[1, 1] = 2
    ca.lattice[1, 2] = 0
    ca.lattice[1, 3] = 1
    ca.lattice[2, 0] = 1
    ca.lattice[2, 1] = 1
    ca.lattice[2, 2] = 0
    ca.lattice[2, 3] = 2
    ca.lattice[3, 0] = 0
    ca.lattice[3, 1] = 1
    ca.lattice[3, 2] = 2
    ca.lattice[3, 3] = 1

    i_count, s_count, r_count = ca.stats()
    assert i_count == 6
    assert s_count == 7
    assert r_count == 3
