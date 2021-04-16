from RomantoInteger import Solution

def test_I():
    sol = Solution()
    assert sol.romanToInt('I') == 1

def test_II():
    sol = Solution()
    assert sol.romanToInt('II') == 2




def test_IV():
    sol = Solution()
    assert sol.romanToInt('IV') == 4
def test_IVIVIV():
    sol = Solution()
    assert sol.romanToInt('IVIVIV') == 12
def test_IVIIVIVI():
    sol = Solution()
    assert sol.romanToInt('IVIIVIVI') == 14

def test_IX():
    sol = Solution()
    assert sol.romanToInt('IX') == 9
def test_IXIXIX():
    sol = Solution()
    assert sol.romanToInt('IXIXIX') == 27
def test_IXIVIVIXI():
    sol = Solution()
    assert sol.romanToInt('IXIVIVIXI') == 27




def test_V():
    sol = Solution()
    assert sol.romanToInt('V') == 5

def test_X():
    sol = Solution()
    assert sol.romanToInt('X') == 10