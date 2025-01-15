import sys

def linear_regression(points):
    n = len(points)
    sum_x = sum_y = sum_xy = sum_x2 = 0
    for x, y in points:
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x2 += x * x
    denominator = n * sum_x2 - sum_x ** 2
    if denominator == 0:
        raise ValueError
    a = (n * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y - a * sum_x) / n
    return a, b

def read_input():
    points = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        x, y = map(float, line.split(","))
        points.append((x, y))
    return points

points = read_input()
a, b = linear_regression(points)
sys.stdout.write(f"{a} {b}\n")