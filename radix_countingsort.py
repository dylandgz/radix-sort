# Define the counting_sort function that takes two arguments:
# - arr: an input list of integers
# - exp: an integer representing the digit position (1s, 10s, 100s, etc.)
def counting_sort(arr, exp):
    n = len(arr)  # Get the length of the input list
    output = [0] * n  # Initialize an output list of the same length as the input list, filled with zeros
    count = [0] * 10  # Initialize a count list to store the frequency of each digit (0-9)

    # Iterate through all elements in the input list
    for i in range(n):
        index = arr[i] // exp  # Calculate the digit at the current position (exp) for the current element (arr[i])
        count[index % 10] += 1  # Increment the count of the current digit (index % 10) in the count list

    # Iterate through the count list, starting from index 1
    for i in range(1, 10):
        count[i] += count[i - 1]  # Update the count list by adding the value of the previous index to the current index

    # Iterate through the input list in reverse order
    i = n - 1
    while i >= 0:
        index = arr[i] // exp  # Calculate the digit at the current position (exp) for the current element (arr[i])
        output[count[index % 10] - 1] = arr[i]  # Place the current element in the output list based on the position determined by the count list
        count[index % 10] -= 1  # Decrement the count of the current digit in the count list
        i -= 1  # Decrement the variable i

    # Iterate through all elements in the output list
    for i in range(n):
        arr[i] = output[i]  # Copy the sorted elements from the output list back to the input list

# Define the radix_sort function that takes an input list of integers (arr) as an argument
def radix_sort(arr):
    max_val = max(arr)  # Get the maximum value in the input list
    exp = 1  # Initialize a variable exp to 1, which will be used to determine the digit position (1s, 10s, 100s, etc.)

    # Continue the loop until all digit positions have been processed
    while max_val // exp > 0:
        counting_sort(arr, exp)  # Call the counting_sort function for the current digit position (exp)
        exp *= 10  # Update the exp variable to move on to the next digit position (1s, 10s, 100s, etc.)

    return arr