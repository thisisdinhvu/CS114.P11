import sys
def count_tablet_sizes(n):
    count = 0
    n_square = n*n
    a_max = int((n_square/2)**0.5) + 1
    for a in range(1, a_max):
        b_square = n_square - a*a
        if b_square > 0:
            b = int(b_square**0.5)
            if b*b == b_square:
                count += 1
    return count

input_data = sys.stdin.read()
n = int(input_data.strip())
print(count_tablet_sizes(n))
# n = int(sys.stdin.read())

# input_data = sys.stdin.read()
#
# # Chuyển input thành số nguyên
# n = int(input_data.strip())
#
# # Tính và in ra kết quả
# print(count_tablet_sizes(n))
