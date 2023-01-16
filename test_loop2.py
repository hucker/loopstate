""" Pytest code for the loopstate2 iterator """

# import pytest
from loopstate import LoopState2, loop_state2


def test_data_class():
    """An used loop state object is the Empty object."""
    state = LoopState2()
    assert state.index == -1
    assert state.first is False
    assert state.last is False


def test_empty():
    """ Test empty sequence """
    for _, state in loop_state2([]):
        assert state.index==1000, "Should not get here"
        if state.index==100:
            break
    else:
        assert True, "Should get here"


def test_single():
    """ Test single sequence """
    for value, state in loop_state2([1]):
        assert value == 1
        assert state.index == 0
        assert state.only is True

def test_double():
    """ Test double sequence and no extra """
    for value, state in loop_state2([1,2]):
        if state.index == 0:
            assert value == 1
        elif state.index == 1:
            assert value == 2
        else:
            assert False

def test_simple_copy():
    """ Test to verify that there are no none values in the list that would
        be here if we were using the more complex loop_state iterator that
        also tracks special cases like empty lists, else conditions, etc. """
    new_list = []
    for value,_ in loop_state2([1,2,3]):
        new_list.append(value)
    assert new_list == [1,2,3]


def test_first_last():
    """ Test simple state tracking """
    for value, state in loop_state2([1,2]):
        if state.index == 0:
            assert value == 1
            assert state.first is True
            assert state.last is False
        elif state.index == 1:
            assert value == 2
            assert state.first is False
            assert state.last is True
        else:
            assert False

def test_first_middle_last():
    """ Test simple state tracking """
    for value, state in loop_state2([1,2,3]):
        if state.index == 0:
            assert value == 1
            assert state.first is True
            assert state.last is False
        elif state.index == 1:
            assert value == 2
            assert state.first is False
            assert state.last is False
        elif state.index == 2:
            assert value == 3
            assert state.first is False
            assert state.last is True
        else:
            assert False
