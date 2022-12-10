# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        output = n

        while not low > high :
            mid = math.floor((low + high) / 2)

            if isBadVersion(mid):
                output = mid
                high = mid - 1
            else:
                low = mid + 1
        return output

            
