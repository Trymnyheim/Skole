# https://open.kattis.com/problems/countingchocolate

from sys import stdin

def main():
    n = int(next(stdin).strip()) # Amount of boxes.. Not needed

    # Creates list of n boxes with x chocolate
    boxes = [int(x) for x in next(stdin).strip().split()]  

    total = sum(boxes) # Sum of all chocolate boxes
    if total % 2 != 0: # Checks if total is divisible by 2
        print("NO")
        return # Cancel if not possible
    
    half = total // 2
    can_sum = [False] * (half + 1)  # DP array
    can_sum[0] = True  

    # Checking if it is possible to achieve half with the boxes
    for chocolate in boxes:
        for j in range(half, chocolate - 1, -1):
            if can_sum[j - chocolate]:
                can_sum[j] = True
    # Print results:
    if can_sum[half]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()