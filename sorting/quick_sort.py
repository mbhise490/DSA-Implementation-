# Problem: Quick Sort
# Average Time Complexity: O(n log n)
# Worst Time Complexity: O(n^2)
# Space Complexity: O(log n)
# Stable: No

def partition(arr, low, high):

    pivot = arr[low]

    i = low
    j = high

    while i < j:

        while arr[i] <= pivot and i < high:
            i += 1

        while arr[j] > pivot and j > low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


def quick_sort(arr, low, high):

    if low < high:

        p_index = partition(arr, low, high)

        quick_sort(arr, low, p_index - 1)

        quick_sort(arr, p_index + 1, high)

    return arr


arr = [3, 4, 2, 4, 3, 4, 2, 3, 42, 3]

print(quick_sort(arr, 0, len(arr) - 1))