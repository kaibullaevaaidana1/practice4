import math
import sys


def dist(x, y):
    return math.hypot(x, y)


def dot(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


def segment_intersects_circle(ax, ay, bx, by, r):
    # projection of origin onto segment AB
    dx = bx - ax
    dy = by - ay
    fx = -ax
    fy = -ay

    t = (fx * dx + fy * dy) / (dx * dx + dy * dy)
    t = max(0, min(1, t))

    closest_x = ax + t * dx
    closest_y = ay + t * dy

    return dist(closest_x, closest_y) < r


def main():
    input_data = sys.stdin.read().strip().split()

    r = float(input_data[0])
    ax, ay = map(float, input_data[1:3])
    bx, by = map(float, input_data[3:5])

    # Straight distance
    straight = math.hypot(ax - bx, ay - by)

    # If no intersection, answer is straight line
    if not segment_intersects_circle(ax, ay, bx, by, r):
        print("{:.10f}".format(straight))
        return

    d1 = dist(ax, ay)
    d2 = dist(bx, by)

    # angle between OA and OB
    cos_theta = dot(ax, ay, bx, by) / (d1 * d2)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    theta = math.acos(cos_theta)

    alpha1 = math.acos(r / d1)
    alpha2 = math.acos(r / d2)

    tangent1 = math.sqrt(d1 * d1 - r * r)
    tangent2 = math.sqrt(d2 * d2 - r * r)

    arc = r * (theta - alpha1 - alpha2)

    result = tangent1 + tangent2 + arc

    print("{:.10f}".format(result))


if __name__ == "__main__":
    main()