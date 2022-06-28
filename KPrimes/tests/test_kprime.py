from kprimes.kprime import FindKPrimes


def test_K2_Start4_End4():
    actual = FindKPrimes(2, 4, 4)
    expected = [4]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_K2_Start143_End143():
    actual = FindKPrimes(2, 143, 143)
    expected = [143]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_K2_Start4_End22():
    actual = FindKPrimes(2, 4, 22)
    expected = [4, 6, 9, 10, 14, 15, 21, 22]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_K3_Start8_End30():
    actual = FindKPrimes(3, 8, 30)
    expected = [8, 12, 18, 20, 27, 28, 30]
    assert actual == expected, f"Expected {expected}, got: {actual}"

def test_K5_Start32_End112():
    actual = FindKPrimes(5, 32, 112)
    expected = [32, 48, 72, 80, 108, 112]
    assert actual == expected, f"Expected {expected}, got: {actual}"