
def main():
    N = 1000000
    streng = input("\nHva skal hashes? Skriv her: ")
    print(hash(streng, N), "\n")


def hash(value, N):
    hash_val = 0
    for ch in value:
        hash_val = hash_val * 31 + ord(ch)
    return hash_val % N

if __name__ == "__main__":
    main()