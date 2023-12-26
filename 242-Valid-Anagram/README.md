# 242. Valid Anagram

## Two Hash map solution
Create two hash maps, one for s and one for t. Populate the hashmaps with the keys as the unique characters in each string and the value as the frequency of those characters. Then compare the values of each character in both hash maps. Make sure to compare size of strings first to only have to loop through once.
TC: O(s+t)
SC: O(s+t)

## Sorting Solution
Simply sort both strings s and t and equate them to eachother. If they are equal, then return true (they are anagrams), else, return false (they are not anagrams).
TC: O(nlogn)
SC: O(1) ~ discuss with interviewer, they will assume sorting takes O(1) but sometimes it takes O(n) depending on the algorithm.