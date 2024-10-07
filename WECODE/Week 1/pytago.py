import math
import sys

def count_tablet_sizes(n):
    count = 0
    n_square = n * n
    a_max = int(math.isqrt(n_square // 2)) + 1
    # (hỏi chat GPT) Sử dụng math.isqrt: Thay vì tính căn bậc hai và chuyển đổi về số nguyên, sử dụng math.isqrt để tính toán căn bậc hai nguyên của số chính phương.
    for a in range(1, a_max):
        a_square = a * a
        b_square = n_square - a_square
        if b_square > 0:
            b = math.isqrt(b_square)
            if b * b == b_square:
                count += 1
    return count

input_data = sys.stdin.read()
n = int(input_data.strip())
print(count_tablet_sizes(n))