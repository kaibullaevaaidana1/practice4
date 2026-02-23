import sys


def main():
    x1, y1 = map(float, sys.stdin.readline().split())
    x2, y2 = map(float, sys.stdin.readline().split())

    # parameter t where line from A to reflected B crosses y=0
    t = y1 / (y1 + y2)

    x = x1 + t * (x2 - x1)

    print(f"{x:.10f} 0.0000000000")


if __name__ == "__main__":
    main()