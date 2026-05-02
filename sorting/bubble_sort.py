# Problem: Bubble Sort
# Time Complexity: O(n^2) (worst/average), O(n) (best case - already sorted)
# Space Complexity: O(1)
# Stable: Yes


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


arr = [3, 4, 2, 4, 3, 4, 2, 3, 42, 3]

print(bubble_sort(arr))