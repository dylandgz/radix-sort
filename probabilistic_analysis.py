import random
import time
import pandas as pd
import numpy as np
import radix_quicksort as quick
import radix_countingsort as counting
import matplotlib.pyplot as plt
import sys
import copy
import pandas as pd

print("Running")

print("recursion depth:", sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print("New recursion depth:", sys.getrecursionlimit())


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


def proabilistic_analysis(input_sizes, num_trials, num_range):
    countsort_prob = []
    quicksort_prob = []
    countsort_true_count = 0
    quicksort_true_count = 0
    for size in input_sizes:
        for i in range(0, num_trials):
            test_list = list_generator(size, num_range)

            test_list2 = copy.deepcopy(test_list)
            test_list3 = copy.deepcopy(test_list)
            # true sorted list
            validation_list = sorted(test_list)
            # counting sort
            sorted_radix_list = counting.radix_sort(test_list2)
            # Quicksort
            sorted_arr_quick = quick.radix_sort_quicksort(test_list3)
            if check_sorted(validation_list, sorted_radix_list):
                countsort_true_count += 1
            if check_sorted(validation_list, sorted_arr_quick):
                quicksort_true_count += 1
        print("Round size: ", size)
        countsort_prob.append(countsort_true_count / num_trials)
        quicksort_prob.append(quicksort_true_count / num_trials)
        countsort_true_count = 0
        quicksort_true_count = 0
    print("countsort probability", countsort_prob)
    print("quicksort probability", quicksort_prob)
    return countsort_prob, quicksort_prob


input_sizes = [2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
num_trials = 100000
num_range = 999
countsort_prob, quicksort_prob = proabilistic_analysis(input_sizes, num_trials, num_range)

# Plot the probabilities
plt.plot(input_sizes, countsort_prob, marker='o', label="Counting Radix Sort")
plt.plot(input_sizes, quicksort_prob, marker='x', label="Radix Quicksort")

# Customize the plot
plt.xlabel("Input Size")
plt.ylabel("Probability")
plt.title("Probabilities of Correct Sorting for Counting Radix Sort and Radix Quicksort")
plt.legend()
plt.grid()

# Create a DataFrame with the results
results_df = pd.DataFrame({
    "Input Size": input_sizes,
    "Counting Radix Sort Probability": countsort_prob,
    "Radix Quicksort Probability": quicksort_prob,
    "Number of Trials": [num_trials] * len(input_sizes),
    "Number range": num_range
})
# Save the DataFrame to a CSV file
results_df.to_csv(f"sort_probs_trials{num_trials}_range{num_range}.csv", index=False)
# Save the plot as an image file (PNG, SVG, or PDF)
plt.savefig(f"sort_probs_plot_{num_trials}_range{num_range}.png", dpi=300)


# Show the plot
plt.show()


print("Finished")
