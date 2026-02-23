import sys

def powers_of_two(n):
    value = 1
    for _ in range(n + 1):
        yield value
        value *= 2

def main():
    n = int(sys.stdin.readline())
    first = True
    for p in powers_of_two(n):
        if first:
            sys.stdout.write(str(p))
            first = False
        else:
            sys.stdout.write(" " + str(p))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()