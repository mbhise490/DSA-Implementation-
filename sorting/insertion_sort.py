# Problem: Insertion Sort
# Time Complexity: O(n^2) (worst/average), O(n) (best case - already sorted)
# Space Complexity: O(1)
# Stable: Yes


def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        c_value = arr[i]   
        p = i              
        while p > 0 and arr[p - 1] > c_value:
            arr[p] = arr[p - 1]
            p = p - 1
        arr[p] = c_value
    return arr

arr = [3, 4, 2, 4, 3, 4, 2, 3, 42, 3]
print(insertion_sort(arr))