# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # the total length of each array passed in
    elements = len(arrA) + len(arrB)
    # creating an array with that total length 
    merged_arr = [0] * elements

    # Your code here
    little_a = 0
    little_b = 0
    index_incrementer = 0

    while little_a < len(arrA) and little_b < len(arrB):
        if arrA[little_a] < arrB[little_b]:
            merged_arr.insert(index_incrementer, arrA[little_a])
            little_a += 1
            index_incrementer += 1
            merged_arr.pop(index_incrementer)
        else:
            merged_arr.insert(index_incrementer, arrB[little_b])
            little_b += 1
            index_incrementer += 1
            merged_arr.pop(index_incrementer)
    while little_b < len(arrB):
        merged_arr.insert(index_incrementer, arrB[little_b])
        little_b += 1
        index_incrementer += 1
        merged_arr.pop(index_incrementer)
    while little_a < len(arrA):
        merged_arr.insert(index_incrementer, arrA[little_a])
        little_a += 1
        index_incrementer += 1
        merged_arr.pop(index_incrementer)

    return merged_arr

a = [1, 4, 7]
b = [2, 3, 8, 9]
print(merge(a, b))

    # I was super close with below
    # as long as the length of arrA AND arrB is more than 0, I want to keep doing this:
    # while len(arrA) > 0 and len(arrB) > 0:
    #     # if the value at the front of arrA is less than the value at the front of arrB
    #     if arrA[0] < arrB[0]:
    #         # save that value
    #         saved = arrA[0]
    #         # then I want to pop that value off of the array
    #         arrA.pop(0)
    #         # I want to also push that element onto the holding array (merged_arr)
    #         merged_arr.append(saved)
    #     # otherwise I want to do the opposite:
    #     if arrB[0] < arrB[0]:
    #         # save the value of arrB
    #         saved = arrB[0]
    #         # pop that value off the array
    #         arrB.pop(0)
    #         # pusht that element onto the holding array
    #         merged_arr.append(saved)
    #     # if the length of arrA is 0
    #     if len(arrA) == 0:
    #         # I want to append arrB onto the end of the merged_arr
    #         merged_arr.append(arrB)
    #     # if the length of arrB is 0
    #     if len(arrB) == 0:
    #         # I want to append arrA onto the end of the merged_arr
    #         merged_arr.append(arrA)

    # return merged_arr



# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # ----------------DIVIDE------------------
    # base case: when the length of the array is greater than 1
    # while len(arr) > 1:  <-------- Almost had it... just was running into infinite loop with while instead of if... I get confused on when to use those...
    if len(arr) > 1:
    # approaching the base case: we need to divide the single array into 2 arrays, which is where we can do that recursively. once there are 2 arrays, each of those arrays will go back through this function and break up/get called until there are only arrays with lengths of 1. 
        right_side = merge_sort(arr[len(arr) // 2:])
        left_side = merge_sort(arr[:len(arr) // 2])

    # -------------------CONQUER------------------ 
    # Base case (same as in the merge helper function above, we're just using it in here)
    # Once there are arrays that are lengths of 1. That's where we can begin to merge them all back together
        arr = merge(right_side, left_side)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
