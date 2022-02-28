# Count the number of characters in the string and store it as key value pair in dicty
#count the number of cahracters in str2 and store it as a value pair in dict2
#compare two key bvalue pair for exactness in comapre statement
#need to check how well it would work
# may be we can use valid parentheses concept here

"""
#242 in leetcode
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""
def isAnagram(self, s: str, t: str):
         if (len(s)!=len(t)):
            return False

         s_sort=sorted(s)
         t_sort=sorted(t)

         for i in range(len(s)):
             if s_sort[i]!=t_sort[i]:
                 return False

         return True

isAnagram("abc","sac")