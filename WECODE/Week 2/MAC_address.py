#import sys
def valid(char):
    return (char in 'ABCDEF1234657890')
def check(mac):
    # if len(mac) > 1000 or ' ' in mac:
    #     return False
    # ps = mac.split('-')
    # if len(ps) != 6:
    #     return False
    # for p in ps:
    #     if len(p)!=2 or not all(char in valid_chars for char in p):
    #         return False
    # return True
    if len(mac) != 17:
        return False
    for i in range(17):
        if i % 3 == 2:
            if mac[i] != '-':
                return False
        else:
            if not valid(mac[i]):
                return False
    return True

# while True:
#     mac = input()
#     if mac == ".":
#         break
#     if check(mac):
#         print("true")
#     else:
#         print("false")
ans = []
mac = input()
while mac != '.':
    if check(mac):
        ans.append('true')
    else:
        ans.append('false')
    mac = input()

for i in ans:
    print(i)