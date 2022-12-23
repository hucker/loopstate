"""
Textual inspired loop state tracker.

This code allows complex loops to be simplified by removing the need for extra
code structures that track state.  The object tracks all of the state for you
and handles all of the special cases making the top level code easier to understand.

The code also reduced the use of exceptions for managing the state of the loop.
The code as been optimized to have zero if statements.  All of the tracking
is done with inline code.

Example usage:

for state,value in loop_state([1,2,3,4]):
    if state.empty:
        print("No data").

    elif state.only:
        print(f"Only item = {value}")

    elif state.first:
        print(f"First item - {value}")

    elif state.last:
        print("fLast Item - {value}")

    elif state.index >= 0:
        print(f" {state.index} Item={value}")


"""
from typing import Iterable, Tuple, TypeVar
from dataclasses import dataclass

type_var = TypeVar("type_var")


@dataclass
class LoopState:
    """State of loop. Initialize to 'empty loop' state """
    first: bool = False
    last: bool = False
    only: bool = False
    empty: bool = True
    index: int = -1

def loop_state(values: Iterable[type_var]) -> Iterable[Tuple[LoopState, type_var]]:
    """
    Iterate and generate state data related to iterating over a sequence.

    By looking at the state variable you can tell if the loop item is
    the first, last, only value in a sequence, if the sequence is empty
    and the index in the sequence.  Tracking this in code is tricky to
    get right.
    """
    state = LoopState()
    
    # Passed None fail gracefully with no exception
    if values is None:
        yield state, None
    
    iter_values = iter(values)

    # Empty Case
    try:
        first = next(iter_values)
    except StopIteration:
        state.empty = True
        yield state, None
        return

    # Single item case
    try:
        state.first = True
        state.index = 0
        state.empty = False
        previous_value = next(iter_values)
        yield state, first

    except StopIteration:
        state.last = True
        state.only = True
        yield state,first
        return

    # Yield everything but the first and last items
    state.first = False
    state.only = False
    for value in iter_values:
        state.index += 1
        yield state, previous_value
        previous_value = value

    # And finally yield the last item
    state.last = True
    state.index += 1
    yield state, previous_value
