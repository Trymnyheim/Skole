import sys

def main():
    filename, _ = sys.argv[1].split(".")
    with open(sys.argv[1], "r") as file:
        input = [int(line.rstrip()) for line in file]
    output = bubbleSort(input)
    with open(filename + "_bubble.out", "w") as file:
        for n in output:
            file.write(str(n) + "\n")


def bubbleSort(A):
    n = len(A)
    for i in range(0, n - 1):
        c = 0
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
            else:
                c += 1
        if c == n - i - 1:
            return A
    return A


if __name__ == "__main__":
    main()
