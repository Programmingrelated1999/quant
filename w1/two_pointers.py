# Two Sum II — Given a sorted array numbers and a target, return the indices (1-indexed) of the two numbers that add up to target. Exactly one solution exists.
# numbers = [2, 7, 11, 15], target = 9 → [1, 2]
def two_sum(nums, target):
    left_idx = 0
    right_idx = len(nums) - 1
    while left_idx < right_idx:
        result = nums[left_idx] + nums[right_idx]
        if result == target:
            return [left_idx + 1, right_idx + 1]
        elif result > target:
            right_idx -= 1
        else: 
            left_idx += 1
    return None

def main():
    nums = [2,7,11,15]
    target = 9
    result = two_sum(nums, target)
    print("Result: ", result)

main()