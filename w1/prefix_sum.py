# The core idea: precompute cumulative sums so any subarray sum is an O(1) lookup instead of O(n).

# Your first problem — fixed:
# Range sum query — given nums, answer multiple queries (i, j) returning the sum of elements from index i to j inclusive.
# nums = [2, 1, 3, 4, 2]
# query(1, 3) → 8
# query(0, 2) → 6

# Build the prefix array first, then answer each query in O(1).

def prefix_sum(nums):
    total = 0
    summed_arr = [0]
    for num in nums:
        total += num
        summed_arr.append(total)
    return summed_arr

def query(summed_arr, i, j):
    return summed_arr[j+1] - summed_arr[i]

def main():
    nums = [2, 1, 3, 4, 2]
    summed_arr = prefix_sum(nums)
    result = query(summed_arr, 1, 3)
    print("Result: ", result)

main()