# All the elements in the array are compared one by one to check if a given element is present in the array or not.
# If element exists then position of the element is returned or -1.

def linear_search(arr: list, ele: int) -> int:
    """
    Serach for given element in the given array
    :param arr: list of elements
    :param ele: element to be searched
    :return: position of the element or -1
    """
    for pos in range(len(arr)):
        if arr[pos] == ele:
            return pos+1

    return -1


if __name__ == "__main__":
    elements = [10, 34, 56, 23, 90, 12, 9, 15]
    element_exists = 23
    element_not_exist = 18

    for e in [element_exists, element_not_exist]:
        pos = linear_search(arr=elements, ele=e)
        if pos == -1:
            print(f"Element {e} does not exist in the given array")
        else:
            print(f"Element {e} exists in the list at position: {pos}")
