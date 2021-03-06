# Sortert fletting av to arrayer
# Input: To sorterte arrayer A1 og A2 og et array A, der |A1| + |A2| = |A| = n
# Output: Et sortert array A med elementene fra A1 og A2
# Notasjon! A1 = minst og A2 = storst
def merge(venstre, hoyre, array):
    i = 0
    j = 0

    while i < len(venstre) and j < len(hoyre):
        if venstre[i] < hoyre[j]:
            array[i + j] = venstre[i]
            i = i + 1
        else:
            array[i + j] = hoyre[j]
            j = j + 1

    while i < len(venstre):
        array[i + j] = venstre[i]
        i = i + 1

    while j < len(hoyre):
        array[i + j] = hoyre[j]
        j = j + 1

    return array

# Merge sort
# Input: Et array A med n elementer
# Output: Et sortert array med de samme n elementene
# Notasjon: A = array
def mergeSort(array):
    n = len(array)
    if n <= 1:
        return array
    i = n/2  # Blir ikke en integer!
    # array[0:int(i)-1], men husk at i-1 bakerst, så vi trenger bare å skrive i
    A1 = mergeSort(array[0:int(i)])
    # array[int(i):n-1], men husk at n-1 betyr bakerst i listen og det får vi med å bare ta n
    A2 = mergeSort(array[int(i):n])
    return merge(A1, A2, array)

# Partition
# Input: Et array A med n elementer, low og high er indekser
# Output: Flytter elementer som er hhv. mindre og større til venstre og høyre enn en gitt index som returneres
def partition(A, low, high):
    #p = choosePivot(A)
    #A[p], A[high] = A[high], A[p]
    pivot = A[high]
    left = low
    right = high - 1

    while left <= right:
        while left <= right and A[left] <= pivot:
            left = left + 1
        while right >= left and A[right] >= pivot:
            right = right - 1
        if left < right:
            A[left], A[right] = A[right], A[left]

    A[left], A[high] = A[high], A[left]
    return left

#QuickSort
#Input: Et array A med n elementer, low og high er indekser
#Output: Et sortert array med de samme n elementene
def quickSort(A, low, high):
    if low >= high:
        return A
    p = partition(A, low, high)
    quickSort(A, low, p - 1)
    quickSort(A, p + 1, high)
    return A


def choosePivot(A):
    x = A[0] - A[len(A) // 2]
    y = A[len(A) // 2] - A[len(A)-1]
    z = A[0] - A[len(A)-1]
    if (x*y > 0):
        return A[len(A) // 2]
    if (x*z > 0):
        return A[len(A)-1]
    return A[0]

#BucketSort
#Input: Et array A med n elementer
#Output: Et array med de samme n elementene sortert etter nøkler
def bucketSort(A):
    pass

listeMedElementer = [3, 7, 1, 12, 34, 76, 23, 444, 8, 4, 5, 6]
print(mergeSort(listeMedElementer))

listeMedElementer = [3, 7, 1, 12, 34, 76, 23, 444, 8, 4, 5, 6]
#listeMedElementer = [3, 7, 1, 9, 11, 0, 2, 10, 8, 4, 5, 6]
print(quickSort(listeMedElementer, 0, len(listeMedElementer)-1))

