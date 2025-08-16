# Jump search works on sorted array. Given array is divided into equal size blocks. First and last element of
# block is compared with element to be searched and then decide whether to go for next block or not. If not moving to
# next block then do linear search in the given block.
# Optimal block size would be sqrt(n)

def jump_search(arr: list, ele: int) -> int:
    low = 0
    high = 3

    while high < len(arr):
        if ele == arr[low]:
            return low
        if ele == arr[high]:
            return high

        if ele > arr[low] and ele > arr[high]:
            low = high
            high += 3

        for i in range(low, high+1):
            if ele == arr[i]:
                return i
        return -1

    return -1


if __name__ == "__main__":
    elements = [1, 3, 5, 7, 9, 11, 13]
    element_exists = 1
    element_not_exist = 8

    for e in [element_exists, element_not_exist]:
        pos = jump_search(elements, e)
        if pos == -1:
            print(f"Element {e} does not exist in the given array")
        else:
            print(f"Element {e} exists in the list at position: {pos}")
