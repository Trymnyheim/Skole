import sys

def main():
    filename, _ = sys.argv[1].split(".")
    with open(sys.argv[1], "r") as file:
        input = [int(line.rstrip()) for line in file]
    output = insertionSort(input)
    with open(filename +"_insertion.out", "w") as file:
        for n in output:
            file.write(str(n)+"\n")
    

def insertionSort(A):
    for i in range(1, len(A)):
        j = i
        while 0 < j and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A


if __name__ == "__main__":
    main()