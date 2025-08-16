# Binary search works on sorted array. Element to be searched is compared first with the middle element.
# If element is greater than mid element then left half of the array is searched, otherwise left half is searrched.
# Best case is O(1), else log(n)

def binary_search(arr: list, ele: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if ele == arr[mid]:
            return mid

        if ele < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    elements = [9, 10, 12, 15, 23, 34, 56, 90]
    element_exists = 23
    element_not_exist = 18

    for e in [element_exists, element_not_exist]:
        pos = binary_search(arr=elements, ele=e)
        if pos == -1:
            print(f"Element {e} does not exist in the given array")
        else:
            print(f"Element {e} exists in the list at position: {pos}")
