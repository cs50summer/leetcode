"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


"""

import re

def remove2(s):
    re.sub(r'\W+','',s)
    print(s)

def remove(s):
    pattern=re.compile(r'[-!\s:,]+')
    return re.sub(pattern,'',s)

def isPalindrome(s):
   #s =remove2(s)
   #s=remove(s)
   #s=''.join(filter(s.isalnum,s))
   #s= ''.join(char for char in s if char.isalnum())
   s= re.sub(r"[^a-zA-Z0-9]", "", s)
   print(s)
   print(s)
   s=s.lower()
   print(s)
   p1=s[0]
   p2=s[-1]
   l=len(s)

   for i in range(l):
       p1 = s[i]
       p2 = s[l-i-1]
       if(p1!=p2):
           return False
       if i + 1 == len(s) // 2:
           break
   return True






print(isPalindrome("Abarat:i on-- a a!!!! fagf"))
print(isPalindrome("A man, a plan, a canal: Panama"))


"""print(s.lower())
print(s)
print(s)
print(remove(s))
s="11 aa aa uu"
#s=s.strip(' ')
print(s)
#s.reverse()
#print(s)


       if s[i]!=s[len-i-1]:
           return False
       if i+1==len(s)//2:
           break
   return True
"""