# In selection sort, given array is divided logically into two parts, sorted and unsorted. From unsorted array, get the
# smallest element and swap it with the element in first of the unsorted array. This also takes O(n*n)

def selection_sort(arr: list) -> None:
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]

    print(f"Sorted array is: {arr}")


if __name__ == "__main__":
    elements = [10, 34, 56, 23, -1, 90, 12, -9, 15]
    selection_sort(elements)
