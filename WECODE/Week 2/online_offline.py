import sys
def check():
    onl_players = set()
    input = iter(sys.stdin.read().split()) # đoạn này em có hỏi chatGPT để tối ưu nhập xuất
    #iter(sys.stdin.read().split()): Đọc toàn bộ dữ liệu một lần và sử dụng iter() để duyệt nhanh hơn.
    res = []
#    output = []
#    result = output.append

    while True:
        a = next(input)
        #next(input_data): Tránh gọi hàm split() nhiều lần, thay vào đó, chúng ta duyệt qua các phần tử với next(), tăng tốc độ cho các thao tác đọc.
        if a == "0":
            break
        a = int(a)
        b = int(next(input))
        if a == 1:
            onl_players.add(b)
        elif a == 2:
            res.append("1\n" if b in onl_players else "0\n")
        elif a == 3:
            onl_players.discard(b)
    sys.stdout.write("".join(res))

check()


