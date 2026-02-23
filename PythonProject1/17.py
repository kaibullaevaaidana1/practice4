import sys
import math


def main():
    input_data = sys.stdin.read().strip().split()

    r = float(input_data[0])
    x1, y1 = map(float, input_data[1:3])
    x2, y2 = map(float, input_data[3:5])

    dx = x2 - x1
    dy = y2 - y1

    # Quadratic coefficients for |A + t(B-A)|^2 = r^2
    a = dx * dx + dy * dy
    b = 2 * (x1 * dx + y1 * dy)
    c = x1 * x1 + y1 * y1 - r * r

    discriminant = b * b - 4 * a * c

    segment_length = math.hypot(dx, dy)

    if discriminant < 0:
        # No intersection: check if fully inside
        if x1 * x1 + y1 * y1 <= r * r and x2 * x2 + y2 * y2 <= r * r:
            print(f"{segment_length:.10f}")
        else:
            print("0.0000000000")
        return

    sqrt_d = math.sqrt(discriminant)

    t1 = (-b - sqrt_d) / (2 * a)
    t2 = (-b + sqrt_d) / (2 * a)

    t_low = max(0.0, min(t1, t2))
    t_high = min(1.0, max(t1, t2))

    if t_low > t_high:
        print("0.0000000000")
        return

    inside_fraction = max(0.0, t_high - t_low)
    result = inside_fraction * segment_length

    print(f"{result:.10f}")


if __name__ == "__main__":
    main()