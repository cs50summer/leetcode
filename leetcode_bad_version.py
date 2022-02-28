"""
ping from 1 to n -- find the band version -- worst case - n times
ping 1 , n , 2, n-1 , 3 , n-2 --- n/2 time

--ping n/2 -- good -- progress towards -- n/2 +1 , bad digress towards n/2 -1 less than n/2
n - 6 versions
n/2 -- call -- good ? call n/2 +1
               bad ? call n/2 -1 3-1=2  -- bad -

call n/2 -- 3 -- good -- 9/2 -- 4 -- good ? -- 4+6/2 -- 5
                 bad -- 3/2 -- 1 --


[1,2,3,4,5,6]     4 is bad
"""
def isBadversion(n):
    if n>=5:
        return True
    else:
        return False

def firstBadVersion(n):

    if(isBadversion(n)==True):
        if n==0 or n==1:
            return 1
        if (n<(n//2)):
            return n
        if(n>(n//2)):
            n=n-1
            return firstBadVersion(n)
    if(isBadversion(n)==False):
        return (n+1)

print(firstBadVersion(9))
