import random
import time
import pandas as pd
import numpy as np
import radix_quicksort as quick
import radix_countingsort as counting
import matplotlib.pyplot as plt
import sys
import copy


# convert decimal to any base less than 10
def dec_to_base(num, base):
    if num == 0:
        return '0'
    base_num = ''
    while num > 0:
        dig = int(num % base)
        base_num += str(dig)
        num //= base

    base_num = base_num[::-1]
    return base_num


def dec_to_base_list(dec_list, base):
    ##### Testing Different Bases
    # convert list to specified base
    test_list_base = []
    for i in dec_list:
        test_list_base.append(dec_to_base(i, base))

    return test_list_base


def str_to_int(str_list):
    int_list = []
    for i in range(0, len(str_list)):
        int_list.append(int(str_list[i]))
    return int_list


def check_sorted(val_arr, arr):
    # print("validation: ", val_arr)
    # print("testing   : ", arr)
    for i, num in enumerate(val_arr):
        # print("Checking comparison: ", num, " and ", arr[i])
        if num != arr[i]:
            return False

    return True


def list_generator(n, num_range):
    rand_list = []
    for i in range(0, n):
        rand_list.append(random.randint(0, num_range))
    return rand_list


print("recursion depth:", sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print("New recursion depth:", sys.getrecursionlimit())


# we are only doing analysis of quicksort, counting sort is trivial because it sorts correctly
def incorrect_sorting_probability_against_numbases(input_sizes, num_trials, num_range, max_num_base):
    quicksort_prob = {}
    quicksort_true_count = 0

    temp_prob=[]
    for size in input_sizes:
        quicksort_prob[size] = []
        print("size : ", size)
        for j in range(2, 11):
            for i in range(0, num_trials):
                test_list = list_generator(size, num_range)
                test_list_base = dec_to_base_list(test_list, j)
                test_list_base = str_to_int(test_list_base)
                test_list2 = copy.deepcopy(test_list_base)
                # true sorted list
                validation_list = sorted(test_list_base)
                # Quicksort radix sort
                sorted_arr_quick = quick.radix_sort_quicksort(test_list2)

                # print("validation         : ", validation_list)
                # print("Quicksort Radix Sort:", sorted_arr_quick)
                if check_sorted(validation_list, sorted_arr_quick):
                    quicksort_true_count += 1
            print("Base: ", j)

            quicksort_prob[size].append(1-(quicksort_true_count / num_trials))

            quicksort_true_count = 0
    print("quicksort probability", quicksort_prob)
    return quicksort_prob


input_sizes = [5,10,15, 20,25]
num_trials = 100000
num_range = 999
max_num_base = 10
num_bases_quicksort_probabilities = incorrect_sorting_probability_against_numbases(input_sizes, num_trials, num_range, max_num_base)
print(num_bases_quicksort_probabilities)
# print("this is base 2 probabilitiesss", num_bases_quicksort_probabilities[2])
num_bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# Plot the probabilities
plt.plot(num_bases, num_bases_quicksort_probabilities[5], marker='+', label="Input Size 5")
plt.plot(num_bases, num_bases_quicksort_probabilities[10], marker='*', label="Input Size 10")
plt.plot(num_bases, num_bases_quicksort_probabilities[15], marker='o', label="Input Size 15")
plt.plot(num_bases, num_bases_quicksort_probabilities[20], marker='x', label="Input Size 20")
plt.plot(num_bases, num_bases_quicksort_probabilities[25], marker='.', label="Input Size 25")



# Customize the plot
plt.xlabel("Number Bases")
plt.ylabel("Probability of Incorrect Sorting")
plt.title("Probabilities of Incorrect Sorting for Radix Quicksort in Different Number Bases")
plt.legend()
plt.grid()


plt.show()