# Bubble sort takes one item and keeps on comparing it with each of ther items and sorts in the correct position.
# Same step is continued for next item and so on. Complexity is O(n*n)

def bubble_sort(arr: list) -> None:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                continue
    print(f"Sorted array is: {arr}")


if __name__ == "__main__":
    elements = [10, 34, 56, 23, 90, -1, 12, 9, 15]
    bubble_sort(elements)
