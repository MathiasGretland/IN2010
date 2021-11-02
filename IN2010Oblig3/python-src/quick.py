def sort(A):

    return QuickSortHelper(A, 0, len(A)-1)
    # Do quicksort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.



def Partition(A, low, high) -> int:
    p: int = ChoosePivot(A, low, high)

    A.swap(high, p)

    pivot = A[high]
    left: int = low
    right: int = high-1

    while left <= right:
        while left <= right and A[left] < pivot:
            left = left + 1

        while right >= left and A[right] >= pivot:
            right = right - 1

        if left < right:
            A.swap(left, right)

    A.swap(left, high)

    return left

def ChoosePivot(A, low, high) -> int:
    return high


def QuickSortHelper(A, low, high) -> list:
    if low >= high:
        return A
    p: int = Partition(A, low, high)

    QuickSortHelper(A, low, p-1)
    QuickSortHelper(A, p+1, high)

    return A



