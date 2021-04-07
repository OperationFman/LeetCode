class Solution:
    def reverse(self, x: int) -> int:
        reverse = int("".join(reversed(str(abs(x)))))
        if x < 0:
            reverse = -abs(reverse)
        min = -2147483648
        max = 2147483647
        if reverse >= min and reverse <= max:
            return reverse
        else:
            return 0