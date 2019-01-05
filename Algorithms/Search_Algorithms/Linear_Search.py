"""
    linear search

    complexity O(n)

    Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    If x matches with an element, return the index.
    If x doesn’t match with any of elements, return -1.
"""

def linearSearch(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1

str_arr = input('Input an array with number and space (ex: XXX XX XX XXX): ').split(' ')
int_arr = list(map(int, str_arr))
target = input('The number you are searching for: ')

print('----------------------------')
print('Your array will be: ', int_arr)
print('Your target will be: ', target)

result = linearSearch(int_arr, len(int_arr), target)
if result == -1:
    print('The number you are looking for is not in array')
else:
    print('Found at index: ', result)
