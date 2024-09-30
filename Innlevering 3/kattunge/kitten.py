from sys import stdin

def main():
    cat = int(next(stdin))
    relations = []
    hasMore = True
    while hasMore:
        input = next(stdin)
        if "-1" in input:
            hasMore = False
        else:
            relations.append([int(x) for x in input.split(" ")])
    path = [cat]
    hasParent = True
    while hasParent:
        hasParent = False
        for r in relations:
            if cat in r[1:]:
                cat = r[0]
                path.append(cat)
                hasParent = True
    for n in path:
        print(n, end=" ")


if __name__ == "__main__":
    main()