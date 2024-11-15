# https://open.kattis.com/problems/findingana

from sys import stdin

def main():
    s = next(stdin).lower().strip()
    for i, l in enumerate(s):
        if l == "a":
            start = i
            break
    print(s[start:])

if __name__ == "__main__":
    main()