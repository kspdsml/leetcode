# 217. Contains Duplicate

## Brute Force Solution
This requires comparing each value in the array to every other value in the array to check for duplicates.  
TC: O(n^2)  
SC: O(1)

## Sorting Solution
This requires sorting the initial array and then iterating through and comparing adjacent values checking for duplicates. This involves using two pointers and shifting the values if there are no duplicates, and returning True if there are duplicates.  
TC: O(nlogn)  
SC: O(1)  

## HashSet Solution
Create a hash set to identify what elements were already seen. When iterating through the array, if the element is not in the hash set, add it to the hash set, and if it is already in the hash set, return True. This solution has the optimal time complexity but has a trade off for space comlexity.  
TC: O(n)  
SC: O(n)  