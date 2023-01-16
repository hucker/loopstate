# loopstate
Textual inspired loop state tracker.

LoopState simplifies complex loop state code by removing code structures
that track state at the point of use.

The low level code operates on iterators and requires no if statements, knowlege
of the lenth of the sequence allowing for generators and 'normal' sequences
to work as expected.

The code below shows a comparison of usage.  While the number of lines of code
is similar, the code that uses the loop_state iterator hides away all of the
bookkeeping so as to minimize the code required to track state.

In the versions that don't use the state tracking the code is doing two things
and it isn't obvious which is which...depending on how much code you've looked at.

Probably more importantly, loop_state can be throughly tested and know that
it handles the edge cases whereas user code might prove far more difficult to
test.


## Examples

### Example 1
Example usage1:

    values = [1,2,3,4]
    for value, state in loop_state(values):
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

Compared to:

    values = [1,2,3,4]

    if not values:
        print("no data")
    else:

        size = len(values)

        if size == 0:
            print("no data")
        elif size == 1:
            print(f"only item = {value}")
        elif
            for index,value in enumerate(values):
                if index == 0:
                    print(f"first value = {value}")
                elif index == size-1:
                    print(f"last value = {value}")
                else:
                    print(f" value{index} = {value})

### Example 2

Even for code that doesn't directly need to track state,
loopstate has a slightly cleaner look because it clearly
separates state tracking and the code, it also allows for
generators to work because it does not need to look at the
length of the sequence in order to see if it is at the end.

Example code:


    count = len(items) - 1
    for index,item in enumerate(items):
        first = (index==0)
        last = (index==count)
        log_item(first, last, item)

or the rather terse code prefered by experienced developers:

    last_index = len(items) - 1
    for index,item in enumerate(items):
        log_item(index==0, index==last_index, item)

Both of these solutions have issues with using the len function which
means a list with all of the items will need to be created...this is
bad in some instances. With generators asking for the length defeats
the entire purpose of having them.  To work without len, the code
would need to implement all/partof the underlying loop state tracking
mechanism.

With looop state you end with this:

    for value,state in loopstate(items):
        log_item(state.first,state.last,value)



