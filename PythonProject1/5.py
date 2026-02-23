import sys


def countdown(n):
    for i in range(n, -1, -1):
        yield i


def main():
    n = int(sys.stdin.readline())

    for value in countdown(n):
        sys.stdout.write(str(value) + "\n")


if __name__ == "__main__":
    main()