from EasyRomantoInteger import Solution

def test_I():
    sol = Solution()
    assert sol.romanToInt('Ie') == 1

def test_II():
    sol = Solution()
    assert sol.romanToInt('IIe') == 2




def test_IV():
    sol = Solution()
    assert sol.romanToInt('IVe') == 4
def test_IVIVIV():
    sol = Solution()
    assert sol.romanToInt('IVIVIVe') == 12
def test_IVIIVIVI():
    sol = Solution()
    assert sol.romanToInt('IVIIVIVIe') == 14

def test_IX():
    sol = Solution()
    assert sol.romanToInt('IXe') == 9
def test_IXIXIX():
    sol = Solution()
    assert sol.romanToInt('IXIXIXe') == 27
def test_IXIVIVIXI():
    sol = Solution()
    assert sol.romanToInt('IXIVIVIXIe') == 27




def test_V():
    sol = Solution()
    assert sol.romanToInt('Ve') == 5

def test_X():
    sol = Solution()
    assert sol.romanToInt('Xe') == 10