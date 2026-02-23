import sys


class Reverse:
    def __init__(self, s):
        self.s = s
        self.index = len(s) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.s[self.index]
        self.index -= 1
        return value


def main():
    s = sys.stdin.readline().rstrip()
    for c in Reverse(s):
        sys.stdout.write(c)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()