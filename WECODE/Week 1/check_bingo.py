def kiemtrabingo(matran, nums):
    # Tạo bảng 3x3
    danhdau = [[False] * 3 for _ in range(3)]

    # Đánh dấu những số đã được rút:
    for i in range(3):
        for j in range(3):
            if matran[i][j] in nums:
                danhdau[i][j] = True

    # Kiểm tra:
    # Các hàng
    for i in range(3):
        count = 0
        for j in range(3):
            if danhdau[i][j]:
                count += 1
        if count == 3:
            return "Yes"

    # Các cột
    for j in range(3):
        count = 0
        for i in range(3):
            if danhdau[i][j]:
                count += 1
        if count == 3:
            return "Yes"

    # Đường chéo chính
    count = 0
    for i in range(3):
        if danhdau[i][i]:
            count += 1
    if count == 3:
        return "Yes"

    # Đường chéo phụ
    count = 0
    for i in range(3):
        if danhdau[i][2 - i]:
            count += 1
    if count == 3:
        return "Yes"
    return "No"

matran = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
nums = [int(input()) for _ in range(N)]
print(kiemtrabingo(matran, nums))