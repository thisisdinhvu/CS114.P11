def check(vps, tbs, tien):
    gia = list(map(int, vps.split()))
    tbs = tbs.strip().split('\n')
    tong_online = sum(gia)
    tong_instore = 0

    for i, tb in enumerate(tbs):
        if 'lower than in-store' in tb:
            try:
                p = float(tb.split('%')[0].split()[-1]) # đoạn này em có hỏi chat cách lấy phần trăm từ đoạn văn bản
                gia_instore = gia[i] / (1 - p / 100)
            except ValueError:
                # Nếu không lấy được giá trị phần trăm, bỏ qua
                gia_instore = gia[i]
        elif 'higher than in-store' in tb:
            try:
                p = float(tb.split('%')[0].split()[-1])
                gia_instore = gia[i] * (1 + p / 100)
            except ValueError:
                # Nếu không lấy được giá trị phần trăm, bỏ qua
                gia_instore = gia[i]
        else:
            gia_instore = gia[i]

        tong_instore += gia_instore

    return tong_online <= tien or tong_instore <= tien

vps = input().strip()
tbs = "\n".join([input().strip() for _ in range(len(vps.split()))])
tien = int(input().strip())

print("true" if check(vps, tbs, tien) else "false")