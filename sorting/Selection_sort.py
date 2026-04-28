# Problem: Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Stable: No

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selection_sort([64, 25, 12, 22, 11]))