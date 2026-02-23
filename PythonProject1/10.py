def cycle_list(lst, n):
    for _ in range(n):
        for item in lst:
            yield item


def main():
    lst = input().split()
    n = int(input())

    print(*cycle_list(lst, n))


if __name__ == "__main__":
    main()