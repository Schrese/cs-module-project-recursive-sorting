# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # Base Case: when the target is found OR when the high/low pointers are at the same index
    # How to get there: increment/decrement depending on the input
    # Conditionals:
    # if the target is found
        # return that index
    # if the target is less than my guess
        # I need to re-run the method while changing start to be the guess - 1 and the end would stay the same
    # if the target is more than my guess
        # I need to re-run the method while changing end to be the guess + 1 and the start would stay the same
    # if the start and end are the same, then that means the target isn't in the list
        # so i just return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

