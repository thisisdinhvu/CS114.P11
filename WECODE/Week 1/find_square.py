def tim_hinh_vuong(A, B):
    xA, yA = A
    xB, yB = B

    # Vector AB
    vx = xB - xA
    vy = yB - yA

    C1 = (xB - vy, yB + vx)
    D1 = (xA - vy, yA + vx)

    C2 = (xB + vy, yB - vx)
    D2 = (xA + vy, yA - vx)

    hinh1 = [A, D1, C1, B]

    hinh2 = [A, B, C2, D2]

    return hinh1, hinh2

xA, yA = map(int, input().split())
xB, yB = map(int, input().split())

h1, h2 = tim_hinh_vuong((xA, yA), (xB, yB))
for hinh in [h1, h2]:
    output = " ".join(f"({x}, {y})" for x, y in hinh)
    print(output)
