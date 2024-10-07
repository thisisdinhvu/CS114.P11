#import sys
def check(str):
    if len(str) > 1 and str[0] == '0':
        return False
    return 0 <= int(str) <= 255
def restore_IP(str):
    temp = []
    n = len(str)
    for i in range(1, min(4, n-2)):
        for j in range(i+1, min(i+4, n-1)):
            for k in range(j+1, min(j+4, n)):
                p1 = str[:i]
                p2 = str[i:j]
                p3 = str[j:k]
                p4 = str[k:]
                if check(p1) and check(p2) and check(p3) and check(p4):
                    temp.append(f"{p1}.{p2}.{p3}.{p4}")
    return temp

#str = sys.stdin.read()
ips = restore_IP(input())
for ip in ips:
    print(ip)
