class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n:
            q, r = divmod(n, 3)
            if (r == 2) or (r and q):
                return False
            n = q
        return True

# Refactor!!