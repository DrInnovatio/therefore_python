from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="sorted", array=array)


def bubblesort(list):

    # Swap the elements to arrange in order
    for iter_num in range(len(list)-1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [19, 2, 31, 45, 6, 11, 121, 27]
bubblesort(list)
print(list)
