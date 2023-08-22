def quicksort(arr, low, high, exp):
    if low < high:
        pi = partition(arr, low, high, exp)
        quicksort(arr, low, pi - 1, exp)
        quicksort(arr, pi + 1, high, exp)

def partition(arr, low, high, exp):
    pivot = (arr[high] // exp) % 10  # Calculate the digit at the current position (exp) for the pivot element
    i = low - 1

    # Iterate through the elements in the range [low, high]
    for j in range(low, high):
        # If the current element's digit is less than or equal to the pivot's digit
        if (arr[j] // exp) % 10 <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# # randomized quicksort
# import random
#
# def quicksort(arr, low, high, exp):
#     if low < high:
#         pi = partition(arr, low, high, exp)
#         quicksort(arr, low, pi - 1, exp)
#         quicksort(arr, pi + 1, high, exp)
#
# def partition(arr, low, high, exp):
#     pivot_idx = random.randint(low, high)  # Choose a random pivot index
#     arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]  # Swap the pivot element with the last element
#     pivot = (arr[high] // exp) % 10  # Calculate the digit at the current position (exp) for the pivot element
#     i = low - 1
#
#     # Iterate through the elements in the range [low, high]
#     for j in range(low, high):
#         # If the current element's digit is less than or equal to the pivot's digit
#         if (arr[j] // exp) % 10 <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# #linear quicksort
# def quicksort(arr, low, high, exp):
#     stack = [(low, high)]
#
#     while stack:
#         low, high = stack.pop()
#
#         if low < high:
#             pi = partition(arr, low, high, exp)
#             stack.extend([(low, pi - 1), (pi + 1, high)])
#
# def partition(arr, low, high, exp):
#     pivot = (arr[high] // exp) % 10
#     i = low - 1
#
#     for j in range(low, high):
#         if (arr[j] // exp) % 10 <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

def radix_sort_quicksort(arr):
    max_val = max(arr)  # Get the maximum value in the input list
    exp = 1  # Initialize a variable exp to 1, which will be used to determine the digit position (1s, 10s, 100s, etc.)

    # Continue the loop until all digit positions have been processed
    while max_val // exp > 0:
        quicksort(arr, 0, len(arr) - 1, exp)  # Call the quicksort function for the current digit position (exp)
        exp *= 10  # Update the exp variable to move on to the next digit position (1s, 10s, 100s, etc.)
        print(f"exp #: {exp}")
        print(f"arr: {arr}")
    return arr



























