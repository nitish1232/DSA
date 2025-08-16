# Heap tree is almost complete binary tree. Which means each node can have 0, 1 or 2 child nodes and child nodes are
# added from left to right. Max heap is special type of heap tree where each parent node is greater than its child
# nodes.
# Tree when represented in array format will have first position empty and root node will be at second position which
# is 1 in array indexing. For each node, its left child is stored at 2n position and right node at 2n+1.
# Insertion in heap takes O(log n) time complexity.
# More info: https://www.youtube.com/watch?v=NEtwJASLU8Q

def insert_to_heap_tree(arr: list, ele: int) -> list:
    arr.append(ele)
    i = len(arr) - 1
    while i > 1:
        parent = i // 2
        print(arr)
        print(i)
        print(parent)
        print(arr[i])
        print(arr[parent])
        print("---------")
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            return arr
    return arr


if __name__ == "__main__":
    array = [None, 70, 60, 65, 45, 39, 40]
    print(f"After inserting {80} to array, it will be: {insert_to_heap_tree(array, 80)}")
