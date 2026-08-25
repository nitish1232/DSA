# Approach:
#     Array is sorted. Hence highest square always comes from highest positive
#     number or lowest negative number. Both of these are at the either end of
#     the given array. Take 2 pointers for either end. Check whichever square
#     is the highest, add it to the answer array. Since we are taking highest
#     square always, start adding result to the answer array from the right.

def square_of_sorted_array_solution_1(arr):
    ans_arr = [i*i for i in arr]
    return sorted(ans_arr)
   
def square_of_sorted_array_solution_2(arr):
    ans_arr = [0] * len(arr)
    i = 0
    j = len(arr) - 1
    k = len(arr) - 1
    while i<=j:
        if arr[i]*arr[i] >= arr[j]*arr[j]:
            ans_arr[k] = arr[i]*arr[i]
            i += 1
        else:
            ans_arr[k] = arr[j]*arr[j]
            j -= 1
        k -= 1
    return ans_arr


arr = [-4,-1,0,3,10]
print(square_of_sorted_array_solution_2(arr))
