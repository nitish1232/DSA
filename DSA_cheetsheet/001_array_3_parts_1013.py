# Approach:
#     Check if sum of all elements is divisible by 3
#     If yes, calculate total sum / 3.
#     Parse through each element keep generating sum. Check if sum is equal to
#     part sum. If yes incerement count of number of parts. If number of parts
#     is 2 and i has not reached last element, then remaining element will
#     sum up to part sum, hence return true.
#     After parsing all elements if number of parts is more than 3 return true,
#     else return False.

def is_3_part_equal_sum(arr):
    if sum(arr) % 3 != 0:
        return False, 0
    part_sum = sum(arr) // 3
    cur_sum = 0
    num_of_parts = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum == part_sum:
            cur_sum = 0
            num_of_parts += 1
            if num_of_parts == 2 and i != len(arr)-1:
                return True, 3
    if num_of_parts >= 3:
        return True, num_of_parts
    else:
        return False, 0


# arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# arr = [0,2,1,-6,6,7,9,-1,2,0,1]
arr = [3,3,6,5,-2,2,5,1,-9,4]
print(is_3_part_equal_sum(arr))
