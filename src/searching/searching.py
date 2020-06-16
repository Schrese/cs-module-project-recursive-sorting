# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # Base Case: when the target is found OR when the high/low pointers are at the same index
    # How to get there: increment/decrement depending on the input
    # Conditionals:
    # print('hello')
    mid = (start + end) // 2
    while start <= end:
        # if the target is found
        if arr[mid] == target:
            # return that index
            return mid
        # if the target is less than my guess
        if target < arr[mid]:
            # I need to re-run the method while changing start to be the guess - 1 and the end would stay the same
            return binary_search(arr, target, start, mid - 1)
        # if the target is more than my guess
        if target > arr[mid]:
            # I need to re-run the method while changing end to be the guess + 1 and the start would stay the same
            return binary_search(arr, target, mid + 1, end)
        # if the start and end are the same, then that means the target isn't in the list
            # so i just return -1
    return -1

# I don't quite know how to have planned the while loop. I planned out literally everything else (with the exception of getting the +1 and -1 backwards). I even wrote down the plan in a notebook, went through it in my head and everything, and I don't understand why I would still need a while loop if I'm using recursion?


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

