"""
    Binary Search:

    Search a sorted array by repeatedly dividing the search interval in half.
    Begin with an interval covering the whole array.
    If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
    Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

    complexity to O(log n).

    We basically ignore half of the elements just after one comparison.

    Compare x with the middle element.
    If x matches with middle element, we return the mid index.
    Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
    Else (x is smaller) recur for the left half.

"""
import math

# Iterative implementation of Binary Search
def binarySearchIterative(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = math.floor((l+r)/2) + 1
        if arr[mid] == x:
            return mid
        # target is small than current mid
        elif x < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return -1


# Test array
int_arr = [ 2, 3, 4, 10, 40 ]
target = 10

"""
idx   0  1  2  3   4
    [ 2, 3, 4, 10, 40 ]

"""
# Function call
result = binarySearchIterative(int_arr, target)


if result != -1:
    print("(Iterative) Element is present at index {}".format(result))
else:
    print("(Iterative) Element is not present in array")

# Recursive implementation of Binary Search
def binarySearchRecursive(arr, x, l, r):
    if r >= 1:
        mid = int((l+r)/2)

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearchRecursive(arr, x, mid+1, r)
        else:
            return binarySearchRecursive(arr, x, l, mid-1)
    else:
        return -1

# Function call
result2 = binarySearchRecursive(int_arr, target, 0, len(int_arr)-1)


if result2 != -1:
    print("(Recursive) Element is present at index {}".format(result2))
else:
    print("(Recursive) Element is not present in array")
