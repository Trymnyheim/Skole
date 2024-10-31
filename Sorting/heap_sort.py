import sys

def main():
    filename = sys.argv[1].split(".")
    with open(sys.argv[1], "r") as file:
        input = [int(line.rstrip()) for line in file]
    output = heapSort(input)
    with open(filename[0]+"_heap.out", "w") as file:
        for n in output:
            file.write(str(n)+"\n")

def heapSort(A):
    buildMaxHeap(A)
    i = len(A) - 1
    while i > 0:
        A[0], A[i] = A[i], A[0]
        bubbleDown(A, 0, i)
        i -= 1
    return A

def buildMaxHeap(A):
    n = len(A)
    i = n // 2 - 1
    while i >= 0:
        bubbleDown(A, i, n)
        i -= 1
    return A

def bubbleDown(A, i, n):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and A[largest] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        bubbleDown(A, largest, n)

if __name__ == "__main__":
    main()