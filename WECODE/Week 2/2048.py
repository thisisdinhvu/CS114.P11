def merge(r):
    new_r = [n for n in r if n != 0]
    merged_r = []
    i = 0
    while i < len(new_r):
        if i < len(new_r) - 1 and new_r[i] == new_r[i + 1]:
            merged_r.append(new_r[i] * 2)
            i += 2
        else:
            merged_r.append(new_r[i])
            i += 1
    merged_r.extend([0] * (4 - len(merged_r)))
    return merged_r

def slide(board, dir):
    if dir == 'L':
        return [merge(r) for r in board]
    elif dir == 'R':
        return [merge(r[::-1])[::-1] for r in board]
    elif dir == 'U':
        new_b = []
        for i in range(4):
            c = [board[j][i] for j in range(4)]
            merged_c = merge(c)
            new_b.append(merged_c)
        return [[new_b[j][i] for j in range(4)] for i in range(4)]
    elif dir == 'D':
        new_b = []
        for i in range(4):
            c = [board[j][i] for j in range(3, -1, -1)]
            merged_c = merge(c)
            new_b.append(merged_c[::-1])
        return [[new_b[j][i] for j in range(4)] for i in range(4)]
    else:
        return board

b = []
for _ in range(4):
    r = list(map(int, input().split()))
    b.append(r)
dir = input().strip()
new_b = slide(b, dir)
for row in new_b:
    print(' '.join(map(str, row)))
