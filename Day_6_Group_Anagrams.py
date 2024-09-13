# Challenge 6 — Group Anagrams
# Problem: Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example: Input: strs = ["eat","tea","tan","ate","nat","bat"] Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs):
        a = defaultdict(list)
        for i in strs:
            s = ''.join(sorted(i))
            a[s].append(i)
        return list(a.values())


# https://leetcode.com/problems/group-anagrams/submissions/1389082660/
