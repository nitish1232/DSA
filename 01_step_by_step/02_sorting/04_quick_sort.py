# An element is considered as pivot element (it could be firdt element, last element or median element). Then array is
# partitioned in such a way that all elements on left side of the pivot are less than or equal to pivot element and
# all elements on the right side are greater. Same logic is applied to left part of the array and then to right part of
# the array

def partition(arr: list, start:int, end:int) -> int:
    pivot = arr[0]
    starting = start
    ending = end
    while starting < ending:
        while arr[starting] <= pivot:
            starting += 1
        while arr[ending] > pivot:
            ending -= 1
        if starting < ending:
            arr[starting], arr[ending] = arr[ending], arr[starting]
    arr[start], arr[ending] = arr[ending], arr[start]
    return ending


# def quick_sort(arr:list, start:int, end:int) -> None:
#     print(f"Array now: {arr}")
#     if start < end:
#         loc = partition(arr, start, end)
#         quick_sort(arr, start, loc-1)
#         quick_sort(arr, loc+1, end)

def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    elements = [10, 34, -13, 56, 18, 0, 23, 90, 12, -9, 15]
    after_sorting = quick_sort(elements)
    print(f"Sorted array is: {after_sorting}")
