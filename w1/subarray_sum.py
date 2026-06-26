# Subarray sum equals k

# Find the total number of contiguous subarrays that sum to k.
# nums = [1, 2, 3], k = 3 → 2 (subarrays [1,2] and [3])
# nums = [1, 1, 1], k = 2 → 2

# Brute force is O(n²) — build every prefix pair. But there's an O(n) solution using a hashmap.
# Hint: if prefix[j] - prefix[i] = k, then prefix[i] = prefix[j] - k. So as you build the prefix sum left to right, 
# ask: how many times have I seen current_sum - k before?
def subarray_sum(nums, k):
    total = 0
    count = 0
    seen = {0: 1}
    for num in nums: 
        total += num
        count += seen.get(total-k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
        
def main():
    nums = [1, 2, 3]
    k = 3
    result = subarray_sum(nums, k)
    print("Result: ", result)

main()