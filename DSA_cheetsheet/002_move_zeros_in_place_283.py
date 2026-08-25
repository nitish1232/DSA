# Approach:
    # Initialize insert_pos to 0. This will track where next non-zero element will go.
    # Iterate through array with i=0. If element at i is not zero and i is not same as
    # insert_pos then swap elemenst at i and insert_pos.
    # Always incerement insert_pos

def move_zeroes(arr):
    insert_pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            if i != insert_pos:
                arr[i], arr[insert_pos] = arr[insert_pos], arr[i]
            insert_pos += 1
    print(arr)


arr = [0,1,0,3,12]
# arr = [0]
# arr = [0, 0, 0, 1, 34, 5, -1, -23, 56]
# arr = [2,1, 3]
move_zeroes(arr)
