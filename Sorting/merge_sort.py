import sys

def main():
    filename, _ = sys.argv[1].split(".")
    with open(sys.argv[1], "r") as file:
        input = [int(line.rstrip()) for line in file]
    output = mergeSort(input)
    with open(filename + "_merge.out", "w") as file:
        for n in output:
            file.write(str(n) + "\n")


def mergeSort(A):
    if len(A) <= 1:
        return A
    i = len(A) // 2
    A1 = mergeSort(A[:i])
    A2 = mergeSort(A[i:])
    return merge(A1, A2, A)


def merge(A1, A2, A):
    i = 0
    j = 0
    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            A[i + j] = A1[i]
            i += 1
        else:
            A[i + j] = A2[j]
            j += 1
    while i < len(A1):
        A[i + j] = A1[i]
        i += 1
    while j < len(A2):
        A[i + j] = A2[j]
        j += 1
    return A


if __name__ == "__main__":
    main()