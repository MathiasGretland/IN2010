
#Input: Et array A med n elementer
#Output: Et sortert Array med de samme n elementene 
def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    
    return A

#Input: Et array A med n elementer
#Output: Et sortert Array med de samme n elementene 
def selectionSort(A):
    n = len(A)
    for i in range(n):
        k = i
        for j in range(i+1, n): # Husk! at n-1 som han skriver i pesudokoden betyr det siste elementet i lista, så vi kan skrive det slikt
            if A[j] < A[k]:
                k = j
        if i != k:
            A[i], A[k] = A[k], A[i] #blir det samme som å skrive det under, det bare passer pseudo kode mye bedre
            """
            temp = A[i]
            A[i] = A[k]
            A[k] = temp
            """

    return A


#Input: Et array A med n elementer
#Output: Et sortert Array med de samme n elementene 
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j = j - 1

    return A

#Hjelpeprosedyre for å bygge en max-heap
#Input: En (uferdig) heap A med n elementer der i er roten
#Output: En mindre uferdig heap
def bubbleDown(A, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and A[largest] < A[left]:
        largest, left = left, largest

    if right < n and A[largest] < A[right]:
        largest, right = right, largest

    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        bubbleDown(A, largest, n)

#Bygger en max-heap
def buildMaxHeap(A):
    n = len(A)
    for i in range(n//2, -1, -1):
        bubbleDown(A, i, n)

#Heapsort
def heapSort(A):
    n = len(A)
    buildMaxHeap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        bubbleDown(A,0,i)

    return A
    
listeMedElementer = [3,7,1,12,34,76,23,444,8,4,5,6]
print(bubbleSort(listeMedElementer))

listeMedElementer = [3,7,1,12,34,76,23,444,8,4,5,6]
print(selectionSort(listeMedElementer))

listeMedElementer = [3,7,1,12,34,76,23,444,8,4,5,6]
print(insertionSort(listeMedElementer))

listeMedElementer = [3,7,1,12,34,76,23,444,8,4,5,6]
print(heapSort(listeMedElementer))