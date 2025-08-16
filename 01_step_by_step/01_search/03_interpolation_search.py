# This search works best on sorted and uniformly distributed array. If array isuniformly distributed, then this search
# takes less number of steps compared to binary serach. Average case is O(log(log(n)))
# pos is calculated as follows pos = low + ((ele-arr[low])/(arr[high]-arr[low])) * (high-low)

def interpolation_search(arr: list, ele: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= ele <= arr[high]:
        position = low + ((ele - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if position < low or position > high:
            return -1

        if ele == arr[position]:
            return position

        if ele < arr[position]:
            high = position - 1
        else:
            low = position + 1
    return -1


if __name__ == "__main__":
    elements = [1, 3, 5, 7, 9, 11, 13]
    element_exists = 7
    element_not_exist = 8

    for e in [element_exists, element_not_exist]:
        pos = interpolation_search(elements, e)
        if pos == -1:
            print(f"Element {e} does not exist in the given array")
        else:
            print(f"Element {e} exists in the list at position: {pos}")
