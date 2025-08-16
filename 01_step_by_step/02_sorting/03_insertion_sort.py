# In selection sort, given array is divided logically into two parts, sorted and unsorted. From unsorted array, get the
# one element and Compare it with all the elements inthe sorted part and find the correct position.
# This also takes O(n*n)

def insertion_sort(arr: list) -> None:
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    print(f"Sorted array is: {arr}")


if __name__ == "__main__":
    elements = [10, 34, 56, 18, 23, 90, 12, -9, 15]
    insertion_sort(elements)
