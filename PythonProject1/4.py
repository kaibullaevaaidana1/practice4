import sys
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
def main():
    a, b = map(int, sys.stdin.readline().split())

    for value in squares(a, b):
        sys.stdout.write(str(value) + "\n")
if __name__ == "__main__":
    main()