import sys
import math


def kahan_sum(numbers):  
    total = 0.0
    c = 0.0
    for num in numbers:
        y = num - c
        t = total + y
        c = (t - total) - y
        total = t
    return total


def linear_reg():
    data = []
    for line in sys.stdin:
        each = line.strip().split(',')
        data.append([float(each[0]), float(each[1])])
    n = len(data)
    x_vals = []
    y_vals = []
    log_x_vals = []
    x_squared = []
    log_x_y = []
    x_y = []
    log_x_x = []
    log_x_squared = []

    for x, y in data:
        log_x = math.log2(x)
        x_vals.append(x)
        y_vals.append(y)
        log_x_vals.append(log_x)
        x_squared.append(x ** 2)
        log_x_y.append(log_x * y)
        x_y.append(x * y)
        log_x_x.append(log_x * x)
        log_x_squared.append(log_x ** 2)

    sigma_x = kahan_sum(x_vals)
    sigma_y = kahan_sum(y_vals)
    sigma_xx = kahan_sum(x_squared)
    sigma_log_x = kahan_sum(log_x_vals)
    sigma_log_y = kahan_sum(log_x_y)
    sigma_xy = kahan_sum(x_y)
    sigma_log_x_x = kahan_sum(log_x_x)
    s_log_x2 = kahan_sum(log_x_squared)

    A = [
        [n, sigma_x, sigma_log_x],
        [sigma_x, sigma_xx, sigma_log_x_x],
        [sigma_log_x, sigma_log_x_x, s_log_x2]
    ]
    B = [sigma_y, sigma_xy, sigma_log_y]

    def gaussian_elimination(A, B):
        n = len(A)
        for i in range(n):
            max_row = i
            v_max = A[max_row][i]
            for k in range(i + 1, n):
                if abs(A[k][i]) > abs(v_max):
                    max_row = k
                    v_max = A[k][i]
            A[i], A[max_row] = A[max_row], A[i]
            B[i], B[max_row] = B[max_row], B[i]
            pivot = (A[i][i])
            for j in range(i, n):
                A[i][j] = (A[i][j]) / pivot
            B[i] = (B[i]) / pivot

            for k in range(i + 1, n):
                factor = A[k][i] / A[i][i]
                for j in range(i + 1, n):
                    A[k][j] -= factor * A[i][j]
                B[k] -= factor * B[i]
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = B[i]
            for j in range(i + 1, n):
                x[i] -= A[i][j] * x[j]
            x[i] = (x[i] / A[i][i])
        return x

    coefficients = gaussian_elimination(A, B)
    a, b, c = coefficients
    print(f"{b}*x + {c}*math.log2(x) + {a}")


linear_reg()