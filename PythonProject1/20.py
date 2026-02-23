import sys


def main():
    input_data = sys.stdin.read().strip().splitlines()
    q = int(input_data[0])

    g = 0
    n = 0

    for i in range(1, q + 1):
        scope, value = input_data[i].split()
        value = int(value)

        if scope == "global":
            g += value
        elif scope == "nonlocal":
            n += value

    print(g, n)


if __name__ == "__main__":
    main()