# The window size isn't fixed; it grows and shrinks based on a condition.
# Longest substring without repeating characters

# Given a string, find the length of the longest substring with no duplicate characters.
# s = "abcabcbb" → 3  (window "abc")
# s = "pwwkew" → 3  (window "wke")
def var_window(s):
    keys = {}
    left_idx = 0
    keys[s[left_idx]] = left_idx
    highest_count = count = 1
    highest_index = 0
    for right_idx in range(1, len(s)):
        if s[right_idx] not in keys:
            keys[s[right_idx]] = right_idx
            count = right_idx - left_idx + 1
            if count > highest_count: 
                highest_count = count
                highest_index = left_idx
        else:
            if left_idx < keys[s[right_idx]] + 1:
                left_idx = keys[s[right_idx]] + 1
            keys[s[right_idx]] = right_idx
            count = right_idx - left_idx + 1
    return s[highest_index: highest_index + highest_count]

def main():
    s = "abcabcbb"
    result = var_window(s)
    print("Result: ", result)

main()