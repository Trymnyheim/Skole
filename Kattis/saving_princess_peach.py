# https://open.kattis.com/problems/princesspeach

from sys import stdin

def main():
    # N = amount of obstacles, Y = amount of identified obstacles
    N, Y = [int(x) for x in next(stdin).strip().split()]

    # Finds identified obstacles
    identified = set()
    for _ in range(Y): 
        identified.add(int(next(stdin).strip()))

    # Goes through all obstacles, i
    for i in range(N):
        if i not in identified: # Print if obstacle not identified
            print(i)

    print(f"Mario got {len(identified)} of the dangerous obstacles.")

if __name__ == "__main__":
    main()