from sys import stdin

def main():
    input = stdin.read().splitlines()
    a = [int(n) for n in input]
    balanced(a)

def balanced(a):
    mid = len(a) // 2
    print(a[mid])
    if len(a) <= 4:
        a.remove(mid)
        for n in reversed(a):
            print(n)
    else:
        high = a[mid+1:]
        low = a[:mid]
        if len(high) <= 2:
            for n in reversed(high):
                print(n)
        else:
            balanced(high)
        if len(low) <= 2:
            for n in reversed(low):
                print(n)
        else:
            balanced(low)

if __name__ == "__main__":
    main()