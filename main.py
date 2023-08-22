import random
import time
import radix_quicksort as quick
import radix_countingsort as counting
import sys
import copy
from collections import Counter




def check_sorted(val_arr, arr):
    # print("validation: ", val_arr)
    # print("testing   : ", arr)
    for i, num in enumerate(val_arr):
        # print("Checking comparison: ", num, " and ", arr[i])
        if num != arr[i]:
            return False

    return True


def list_generator(n):
    list = []
    for i in range(0, n):
        list.append(random.randint(0, 100))
    return list


print("recursion depth:", sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print("New recursion depth:", sys.getrecursionlimit())

# Example with random generated values
n = 5

# test_list = list_generator(n)
test_list =[98,13,45,64,76,81,37,52,29,0]
random.shuffle(test_list)

# test_list=[0,19,4,1305,12,1004,15,11,16,64,1300,1367,1365,29]
test_list2 = copy.deepcopy(test_list)
test_list3 = copy.deepcopy(test_list)
print("Is running")


# print("Test list:", test_list)
validation_list = sorted(test_list)
# print("Validation list:", validation_list)

start = time.time()
sorted_radix_list = counting.radix_sort(test_list2)
end = time.time()
sort_time = end - start
print("Total sort time with radix counting sort: ", sort_time)
# print("sorted array:   ", sorted_radix_list)

start = time.time()
sorted_arr_quick = quick.radix_sort_quicksort(test_list3)
end = time.time()
sort_time = end - start
print("Total sort time with radix quicksort: ", sort_time)
# print("sorted array:   ", sorted_arr_quick)
print (test_list)
print("===========================================================")
print("Is counting sort sorted?:", "Yes" if check_sorted(validation_list, sorted_radix_list) else "No")
print (sorted_radix_list)
print("===========================================================")
print("Is quicksort sorted?:", "Yes" if check_sorted(validation_list, sorted_arr_quick) else "No")
print (sorted_arr_quick)




