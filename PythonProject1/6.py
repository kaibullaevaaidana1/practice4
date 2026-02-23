import sys

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    n = int(sys.stdin.readline())
    first = True
    for num in fibonacci(n):
        if first:
            sys.stdout.write(str(num))
            first = False
        else:
            sys.stdout.write("," + str(num))

if __name__ == "__main__":
    main()