# Problem: Merge Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Stable: Yes


def merge(left, right):

    result = []

    l, r = len(left), len(right)

    m, n = 0, 0

    while m < l and n < r:

        if left[m] < right[n]:
            result.append(left[m])
            m += 1

        else:
            result.append(right[n])
            n += 1

    while m < l:
        result.append(left[m])
        m += 1

    while n < r:
        result.append(right[n])
        n += 1

    return result


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


arr = [3, 4, 2, 4, 3, 4, 2, 3, 42, 3]

print(merge_sort(arr))