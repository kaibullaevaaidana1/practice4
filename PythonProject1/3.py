import sys

def gen(n):
    i = 0
    while i <= n:
        yield i
        i += 12

n = int(input())
first = True
for x in gen(n):
    if first:
        sys.stdout.write(str(x))
        first = False
    else:
        sys.stdout.write(' ' + str(x))
sys.stdout.write('\n')