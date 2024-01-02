# 1. Two Sum

## Brute Force Solution
Check every combination of two values and see if they can sum up to the target.
TC: O(n^2)
SC: O(1)

## Hashmap Solution
Map values to index. Look for complement between current value and target in hashmap, and return current index and complement index.