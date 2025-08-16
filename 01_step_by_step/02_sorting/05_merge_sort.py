# Merge sort https://www.youtube.com/watch?v=jlHkDBEumP0
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


if __name__ == "__main__":
    elements = [10, 34, -12, 56, 18, 0, 23, 90, 12, -9, 15]
    after_sorting = merge_sort(elements)
    print(f"Sorted array is: {after_sorting}")