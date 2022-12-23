Textual inspired loop state tracker.

LoopState simplifies complex code by removing code structures that track state.  
The low level code ooperates on iterators and requires no if statements. The
state of the iterator visible in properties so top level code is more readable.

The code below shows a comparison of usage.  While the number of lines of code
is similar, the code that uses the loop_state iterator hides away all of the
bookkeeping so it is clear that belongs to what in the body of the loop.

In the versions that don't use the state tracking the code is doing two things
and it isn't clear which is which...depending on how much code you've looked at.

Probably more importantly, loop_state can be throughly tested and know that
it handles the edge cases whereas user code might prove far more difficult to
test.


Example usage1:

    values = [1,2,3,4]
    for state,value in loop_state(values):
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

Example code:

    api->. draw_item(is_first, is_last, item)
    
    for state,item in loop_state(items):
        draw_item(state.first,state.last,item)
        
Compared to:

    count = len(items)
    for index,item in enumerate(items):
        first = (index==0)
        last = (index==count-1)
        draw_item(first,last,item)
        
or the rather terse:
    
    count = len(items)
    for index,item in enumerate(items):
        draw_item(index==0,index==count-1,item)
    
    

        
