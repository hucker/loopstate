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
