# Problem: Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Stable: No


def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        p=i
        for j in range(i+1,n):
            if arr[j]<arr[p]:
                p=j
        if p!=i:
            arr[i],arr[p]=arr[p],arr[i]
    return arr

arr=[5,3,24,5,3,74,3,7,44,8,9,8,7]

print(selection_sort(arr))
