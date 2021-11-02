
def BucketSort(A, digit, base) -> list:
    B: list = []
    n: int = len(A)

    for i in range(base):
        B.append([])

    for i in range(n):
        k: int = get_digit(A[i], digit)
        B[k].append(A[i])

    j: int = 0
    for k in range(len(B)):
        for x in B[k]:
            A[j] = x
            j = j+1

    return A


def get_digit(number, n) -> int:
    return number // 10**n % 10


def sort(A) -> list:
    d: int = mostDigits(A)

    for i in range(d):
        A = BucketSort(A, i, 10)

    return A


def mostDigits(A) -> int:
    maxDigits: int = 0

    for x in A:
        maxDigits = max(maxDigits, len(str(x)))

    return maxDigits
