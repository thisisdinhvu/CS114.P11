    a,b = input()
    c,d = input()

    check_sotramkenhau = (a == '#' and b == '#') + (a == '#' and c == '#') + (b == '#' and d == '#') + (c == '#' and d == '#')
    tongsotram = [a,b,c,d].count('#')

    if tongsotram >=2 and check_sotramkenhau > 0:
        print('Yes')
    else:
        print('No')

