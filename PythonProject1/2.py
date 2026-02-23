import sys

def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(sys.stdin.readline())

first = True
for num in even_generator(n):
    if first:
        sys.stdout.write(str(num))
        first = False
    else:
        sys.stdout.write("," + str(num))