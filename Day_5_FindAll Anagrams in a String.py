# Challenge 5 — Find All Anagrams in a String
# Given two strings s and p, return all the start indices of p's anagrams in s. The answer can be in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example: Input: s = "cbaebabacd", p = "abc" Output: [0,6] Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc". The substring with start index = 6 is "bac", which is an anagram of "abc".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r=len(p)
        l=[]
        l1=[]
        l2=[]
        for i in s:
            l.append(i)
        for j in p:
            l2.append(j) 
        l2.sort()          
        for i in range(len(l)-r+1):
            jk=l[i:r]
            jk.sort()
            if jk==l2:
                l1.append(i)
            r+=1
        return l1

# https://leetcode.com/problems/find-all-anagrams-in-a-string
