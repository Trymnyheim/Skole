# https://open.kattis.com/problems/stockprices

# Passes test-case 1 but run-time error on test case 2

from sys import stdin
from heapq import heappush, heappop

def main():
    N = int(next(stdin)) # Amount of cases
    cases = []
    for _ in range(N): 
        order = []
        n = int(next(stdin)) # Amount of lines in each case
        for _ in range(n): 
            line = next(stdin).strip().split() # Read each buy/sell order
            order.append(line)
        cases.append(order) # Adds each case to list of cases
    
    # Perform each order for each case
    for case in cases:
        calculate_prices(case)


def calculate_prices(case):
    asks = []  # Min-heap
    bids = []  # Max-heap
    stock = "-"  # Last transaction price
    for order in case:
        order_type, x, _, _, y = order
        x = int(x)
        y = int(y)
        if order_type == "buy":
            heappush(bids, (-y, x))
            while asks and (-bids[0][0]) >= asks[0][0]:  # Match orders
                stock = make_transaction(asks, bids)
        elif order_type == "sell":
            heappush(asks, (y, x))
            while bids and asks and asks[0][0] <= -bids[0][0]:  # Match orders
                stock = make_transaction(asks, bids)

        # Output after each order:
        ask = asks[0][0] if asks else "-"
        bid = -bids[0][0] if bids else "-"
        print(ask, bid, stock)


def make_transaction(asks, bids):
    stock = "-"
    while asks and bids and asks[0][0] <= -bids[0][0]:
        ask_price, ask_n = heappop(asks)
        bid_price, bid_n = heappop(bids)
        stock = ask_price  # The price at which the transaction happens

        # Adjusting the quantities of shares:
        if ask_n > bid_n:
            ask_n -= bid_n
            heappush(asks, (ask_price, ask_n))
        elif bid_n > ask_n:
            bid_n -= ask_n
            heappush(bids, (bid_price, bid_n))
    return stock


if __name__ == "__main__":
    main()