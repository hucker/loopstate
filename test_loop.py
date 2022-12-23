from loopstate import LoopState,loop_state


def test_data_class():
    """ An used loop state object is the Empty object."""
    state = LoopState()
    assert state.empty is True
    assert state.index == -1
    assert state.first is False
    assert state.only is False
    assert state.last is False


def test_empty():
    """ Empty list """
    values = []

    for state, _ in loop_state(values):
        assert state.empty is True
        assert state.index == -1
        assert state.first is False
        assert state.only is False
        assert state.last is False


def test_single():
    """ Single item list - only """
    values = [1]

    for state, value in loop_state(values):
        assert state.empty is False
        assert state.index == 0
        assert state.first is True
        assert state.only is True
        assert state.last is True
        assert value == 1


def test_more_than_two():
    """ Normal list with beginning middle and end"""
    values = [1, 2, 3]
    seq = loop_state(values)
    state, value = next(seq)
    assert state.empty is False
    assert state.index == 0
    assert state.first is True
    assert state.only is False
    assert state.last is False
    assert value == 1

    state, value = next(seq)
    assert state.empty is False
    assert state.index == 1
    assert state.first is False
    assert state.only is False
    assert state.last is False
    assert value == 2

    state, value = next(seq)
    assert state.empty is False
    assert state.index == 2
    assert state.first is False
    assert state.only is False
    assert state.last is True
    assert value == 3


def test_normal_empty_use_case():
    for state, _ in loop_state([]):
        assert state.empty is True
        assert state.index == -1
        assert state.first is False
        assert state.last is False
        assert state.only is False


def test_normal_single_time_case():
    for state, value in loop_state([1]):
        if value == 1:
            assert state.first is True
            assert state.only is True
            assert state.last is True
            assert state.index == 0


def test_normal_more_than_two_case():
    for state, value in loop_state([1, 2, 3]):
        if value == 1:
            assert state.first is True
            assert state.only is False
            assert state.last is False
            assert state.index == 0
        elif value == 2:
            assert state.first is False
            assert state.only is False
            assert state.last is False
            assert state.index == 1
        elif value == 3:
            assert state.first is False
            assert state.only is False
            assert state.last is True
            assert state.index == 2


def test_loop_case2():
    for state, value in loop_state([1, 2, 3]):
        if state.first:
            assert value == 1
            assert state.only is False
        if state.last:
            assert value == 3
        if state.index == 0:
            assert value == 1
            assert state.first is True
            assert state.last is False
            assert state.only is False
        if state.index == 1:
            assert value == 2
        if state.index == 2:
            assert value == 3
            assert state.last is True
            assert state.first is False


def test_loop_case3():
    for state, _ in loop_state([]):
        assert state.empty is True


def test_loop_case1():
    for state, value in loop_state([1]):
        assert state.empty is False
        assert state.only is True
        assert state.first is True
        assert state.last is True
        assert state.index == 0
        assert value == 1


def test_loop_gen_1():
    seq = range(1)
    for state, value in loop_state(seq):
        assert state.empty is False
        assert state.only is True
        assert state.first is True
        assert state.last is True
        assert state.index == 0
        assert value == 0


def test_loop_gen_2():
    seq = range(2)
    for state, value in loop_state(seq):
        if state.index == 0:
            assert state.empty is False
            assert state.only is False
            assert state.first is True
            assert state.last is False
            assert state.index == 0
            assert value == 0
        if state.index == 1:
            assert state.empty is False
            assert state.only is False
            assert state.first is False
            assert state.last is True
            assert state.index == 1
            assert value == 1
