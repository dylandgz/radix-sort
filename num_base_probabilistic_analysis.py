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
def probabilistic_analysis_against_input(input_sizes, num_trials, num_range, max_num_base):
    quicksort_prob = {}
    quicksort_true_count = 0
    for j in range(2, max_num_base + 1):
        quicksort_prob[j] = []
        print("Number base round: ", j)
        for size in input_sizes:
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
            print("Round size: ", size)

            quicksort_prob[j].append(quicksort_true_count / num_trials)

            quicksort_true_count = 0
    print("quicksort probability", quicksort_prob)
    return quicksort_prob


input_sizes = [2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
num_trials = 10000
num_range = 999
max_num_base = 10
num_bases_quicksort_probabilities = probabilistic_analysis_against_input(input_sizes, num_trials, num_range, max_num_base)
print(num_bases_quicksort_probabilities)
print("this is base 2 probabilitiesss", num_bases_quicksort_probabilities[2])
num_bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# Plot the probabilities
plt.plot(input_sizes, num_bases_quicksort_probabilities[2], marker='o', label="Base 2")
plt.plot(input_sizes, num_bases_quicksort_probabilities[3], marker='x', label="Base 3")
plt.plot(input_sizes, num_bases_quicksort_probabilities[4], marker='.', label="Base 4")
plt.plot(input_sizes, num_bases_quicksort_probabilities[5], marker='d', label="Base 5")
plt.plot(input_sizes, num_bases_quicksort_probabilities[6], marker='X', label="Base 6")
plt.plot(input_sizes, num_bases_quicksort_probabilities[7], marker='+', label="Base 7")
plt.plot(input_sizes, num_bases_quicksort_probabilities[8], marker='*', label="Base 8")
plt.plot(input_sizes, num_bases_quicksort_probabilities[9], marker='8', label="Base 9")
plt.plot(input_sizes, num_bases_quicksort_probabilities[10], marker='4', label="Base 10")


# Customize the plot
plt.xlabel("input_sizes")
plt.ylabel("Probability")
plt.title("Probabilities of Correct Sorting for Radix Quicksort in Different Input Sizes")
plt.legend()
plt.grid()


plt.show()