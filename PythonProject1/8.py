import sys
import math

def primes_up_to(n):
    if n < 2:
        return
    for num in range(2, n + 1):
        is_prime = True
        limit = int(math.isqrt(num)) + 1
        for i in range(2, limit):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

def main():
    n = int(sys.stdin.readline())
    first = True
    for p in primes_up_to(n):
        if first:
            sys.stdout.write(str(p))
            first = False
        else:
            sys.stdout.write(" " + str(p))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()