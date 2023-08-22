import random
import radix_quicksort as quick
import radix_countingsort as counting
from memory_profiler import profile
import sys

print("recursion depth:", sys.getrecursionlimit())
sys.setrecursionlimit(20000)
print("New recursion depth:", sys.getrecursionlimit())



# @profile
# def measure_counting_sort(arr):
#     return counting.radix_sort(arr)

@profile
def measure_quick_sort(arr):
    return quick.radix_sort_quicksort(arr)



if __name__ == "__main__":
    random.seed(42)
    test_data = [random.randint(0, 10000) for _ in range(10000)]

    # measure_counting_sort(test_data[:])
    measure_quick_sort(test_data[:])

#mprof run memory_benchmark.py
#mprof plot
