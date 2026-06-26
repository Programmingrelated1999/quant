# The core idea: maintain a window [left, right] that expands and shrinks based on 
# a condition — avoids recomputing from scratch each step.

# nums = [2, 1, 5, 1, 3, 2],  k = 3  (sum of window size 3)
# [2, 1, 5], 1, 3, 2   → sum = 8
#  2, [1, 5, 1], 3, 2  → sum = 7   (slide: -2, +1)
#  2, 1, [5, 1, 3], 2  → sum = 9   (slide: -1, +3)
#  2, 1, 5, [1, 3, 2]  → sum = 6   (slide: -5, +2)

# Maximum sum subarray of size k
# nums = [2, 1, 5, 1, 3, 2], k = 3 → 9

def sliding_window(nums, k):
    max_sum = 0
    for i in range(k):
        max_sum += nums[i]
    curr_sum = max_sum
    left_idx = 0
    right_idx = k-1
    while (right_idx+1) < len(nums):
        curr_sum = curr_sum - nums[left_idx] + nums[right_idx+1]
        if curr_sum > max_sum:
            max_sum = curr_sum
        left_idx += 1
        right_idx += 1
    return max_sum

def main():
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    result = sliding_window(nums, k)
    print("Result: ", result)

main()
