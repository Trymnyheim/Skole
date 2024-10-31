import sys
import time

def main():
    filename, _ = sys.argv[1].split(".")
    with open(sys.argv[1], "r") as file:
        input = [int(line.rstrip()) for line in file]
    commands = sys.argv[2:]
    if commands[0] == "sort":
        sort(input, filename, commands[1:])
    if commands[0] == "stats":
        generateStats(input, filename, commands[1:])


def sort(input, filename, com):
    if "insert" in com:
        writeOutput(insertionSort(input), filename + "_insertion.out")
    if "merge" in com:
        writeOutput(mergeSort(input), filename + "_merge.out")
    if "heap" in com:
        writeOutput(heapSort(input), filename + "_heap.out")
    if "bubble" in com:
        writeOutput(bubbleSort(input), filename + "_bubble.out")


def generateStats(A, filename, com):
    # Creating statistic objects
    headers = ["n"]
    if "insert" in com:
        insertS = Stats("insert")
        headers.append(insertS.getHeaders())
    if "merge" in com:
        mergeS = Stats("merge")
        headers.append(mergeS.getHeaders())
    if "heap" in com:
        heapS = Stats("heap")
        headers.append(heapS.getHeaders())
    if "bubble" in com:
        bubbleS = Stats("bubble")
        headers.append(bubbleS.getHeaders()) 
    # Performing analysis
    output = []
    i = 0
    while i <= len(A):
        out = [i]
        if "insert" in com:
            insertS.reset()
            t = time.perf_counter()
            insertionSort(A[:i], insertS)
            t = (time.perf_counter() - t) *(10**6)
            insertS.setTime(t)
            for value in insertS.get():
                out.append(value)
        if "merge" in com:
            mergeS.reset()
            t = time.perf_counter()
            mergeSort(A[:i], mergeS)
            t = (time.perf_counter() - t) *(10**6)
            mergeS.setTime(t)
            for value in mergeS.get():
                out.append(value)
        if "heap" in com:
            heapS.reset()
            t = time.perf_counter()
            heapSort(A[:i], heapS)
            t = (time.perf_counter() - t) *(10**6)
            heapS.setTime(t)
            for value in heapS.get():
                out.append(value)
        if "bubble" in com:
            bubbleS.reset()
            t = time.perf_counter()
            bubbleSort(A[:i], bubbleS)
            t = (time.perf_counter() - t) *(10**6)
            bubbleS.setTime(t)
            for value in bubbleS.get():
                out.append(value)
        output.append(out)
        i += round((len(A) / 10) + 0.4)
    writeCSV(output, headers, f"{filename}_stats.csv")
    return output


def writeOutput(output, filename):
    with open(filename, "w") as file:
        for n in output:
            file.write(str(n) + "\n")

def writeCSV(output, headers, filename):
    with open(filename, "w", encoding="utf8") as file:
        header = ""
        for h in headers:
            header += (str(h) + ",")
        file.write(header[:len(header)-1] + "\n")
        for list in output:
            line = ""
            for n in list:
                line += str(n) + ","
            file.write(line[:len(line)-1] + "\n")


def mergeSort(A, S = None):
    if len(A) <= 1:
        return A
    i = len(A) // 2
    A1 = mergeSort(A[:i], S)
    A2 = mergeSort(A[i:], S)
    return merge(A1, A2, A, S)


def merge(A1, A2, A, S):
    i = 0
    j = 0
    while i < len(A1) and j < len(A2):
        if lessThan(A1[i], A2[j], S):
            A[i + j] = A1[i]
            if i != i + j and S:
                S.incSwaps()
            i += 1
        else:
            A[i + j] = A2[j]
            if S:
                S.incSwaps()
            j += 1
    while i < len(A1):
        A[i + j] = A1[i]
        if S:
            S.incSwaps()
        i += 1
    while j < len(A2):
        A[i + j] = A2[j]
        if S:
            S.incSwaps()
        j += 1
    return A


def insertionSort(A, S = None):
    for i in range(1, len(A)):
        j = i
        while j > 0 and lessThan(A[j], A[j-1], S):
            A[j], A[j-1] = A[j-1], A[j]
            if S:
                S.incSwaps()
            j -= 1
    return A


def bubbleSort(A, S = None):
    n = len(A)
    for i in range(0, n - 1):
        c = 0
        for j in range(0, n - i - 1):
            if lessThan(A[j + 1], A[j], S):
                if S:
                    S.incSwaps()
                A[j], A[j + 1] = A[j + 1], A[j]
            else:
                c += 1
        if c == n - i - 1:
            return A
    return A


def heapSort(A, S = None):
    buildMaxHeap(A, S)
    i = len(A) - 1
    while 0 < i:
        A[0], A[i] = A[i], A[0]
        if S:
            S.incSwaps()
        bubbleDown(A, 0, i, S)
        i -= 1
    return A


def buildMaxHeap(A, S):
    n = len(A)
    i = n // 2 - 1
    while 0 <= i:
        bubbleDown(A, i, n, S)
        i -= 1
    return A


def bubbleDown(A, i, n, S):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and lessThan(A[largest], A[left], S):
        largest = left
    if right < n and lessThan(A[largest], A[right], S):
        largest = right
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        if S:
            S.incSwaps()
        bubbleDown(A, largest, n, S)


def lessThan(x, y, alg):
    if alg != None:
        alg.incCmp()
    return x < y


class Stats:
    def __init__(self, name):
        self.name = name
        self.cmp = 0
        self.swaps = 0
        self.time = 0
    
    def incCmp(self):
        self.cmp += 1

    def incSwaps(self):
        self.swaps += 1

    def setTime(self, time):
        self.time = round(time)

    def __str__(self):
        return f"{self.cmp},{self.swaps},{self.time}"
    
    def get(self):
        return [self.cmp, self.swaps, self.time]
    
    def getHeaders(self):
        n = self.name
        return f"{n}_cmp,{n}_swaps,{n}_time"
    
    def reset(self):
        self.cmp = 0
        self.swaps = 0
        self.time = 0


if __name__ == "__main__":
    main()