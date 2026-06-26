# Find all unique triplets that sum to zero.
# nums = [-1, 0, 1, 2, -1, -4] → [[-1, -1, 2], [-1, 0, 1]]
def three_sum_zero(nums):
    nums.sort()
    start_idx = 0
    right_idx = len(nums) - 1
    left_idx = start_idx + 1
    combinations = []
    while start_idx < len(nums) - 2:
        if start_idx > 0 and nums[start_idx] == nums[start_idx-1]:
            start_idx += 1
            continue
        while left_idx < right_idx:
            result = nums[start_idx] + nums[left_idx] + nums[right_idx]
            if result == 0:
                combinations.append([nums[start_idx], nums[left_idx], nums[right_idx]])
                left_idx += 1
                right_idx -= 1
            elif result > 0:
                right_idx -= 1
            else: 
                left_idx += 1
        start_idx += 1
        left_idx = start_idx + 1
        right_idx = len(nums) - 1
    return combinations

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum_zero(nums)
    print("Result: ", result)

main()