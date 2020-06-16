# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # the total length of each array passed in
    elements = len(arrA) + len(arrB)
    # creating an array with that total length 
    merged_arr = [0] * elements

    # Your code here
    # as long as the length of arrA AND arrB is more than 0, I want to keep doing this:
        # if the value at the front of arrA is less than the value at the front of arrB
            # save that value
            # then I want to pop that value off of the array
            # I want to also push that element onto the holding array (merged_arr)
        # otherwise I want to do the opposite:
            # save the value of arrB
            # pop that value off the array
            # pusht that element onto the holding array
        # if the length of arrA is 0
            # I want to append arrB onto the end of the merged_arr
        # if the length of arrB is 0
            # I want to append arrA onto the end of the merged_arr

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

