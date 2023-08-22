import random
import time
import pandas as pd
import numpy as np
import radix_quicksort as quick
import radix_countingsort as counting
import matplotlib.pyplot as plt
import sys
import copy


# binary_numbers = [
#     "10101010",
#     "11001100",
#     "10010100",
#     "11110000",
#     "01010101",
#     "00110011",
#     "00001111",
#     "10110011",
#     "01100110",
#     "11011011",
#     "101",
#     "11111110",
#     "11111111111"
# ]

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


def list_generator(n):
    list = []
    for i in range(0, n):
        list.append(random.randint(0, 100))
    return list


print("recursion depth:", sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print("New recursion depth:", sys.getrecursionlimit())

# n = 5
# base=2
# test_list = []
# test_list = list_generator(n)
# # test_list=dec_to_base()
# test_list_base = dec_to_base_list(test_list, base)
# test_list_base= str_to_int(test_list_base)
#
# print("this is base 10:", test_list)
# print(f"this is base {base}:", test_list_base)
# # print("this is base 2 SORTED:", sorted(test_list_base))
#
# test_list2 = copy.deepcopy(test_list_base)
# test_list3 = copy.deepcopy(test_list_base)


# sorted_base_numbers = sorted(test_list_base)
# # counting sort
# sorted_radix_list = counting.radix_sort(test_list_base)
# # Quicksort
# sorted_arr_quick = quick.radix_sort_quicksort(test_list3)
#
# print("validation         : ", sorted_base_numbers)
# print("Counting Radix Sort: ", sorted_radix_list)
# print("Quicksort Radix Sort:", sorted_arr_quick)
#

#just testing sorting for base 10
base_8_nums = [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23]
random.shuffle(base_8_nums)
print(base_8_nums)



print(sorted(base_8_nums))
