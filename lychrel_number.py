# def check_palindrome(n):
#     s = str(n)
#     return s == s[::-1]
#
# # def func(n):
# #     return n + int(str(n)[::-1])
#
# def check_lychrel(n):
#     count = 0
#     results = []
#     while count <= 10000 and len(str(n)) <= 15000:
#         if check_palindrome(n):
#             print("NO")
#             # for result in results:
#             #     print(result)
#             print('\n'.join(map(str, results)))
#             print(n)
#             return
#         results.append(n)
#         n += int(str(n)[::-1])
#         count += 1
#
#     print("YES")
#     print(count)
#     print(n)
#
# n = int(input().strip())
# check_lychrel(n)
def is_palindrome(n):
    """Check if a number is a palindrome."""
    s = str(n)
    return s == s[::-1]


def reverse_number(n):
    """Return the reverse of a number."""
    return int(str(n)[::-1])


def lychrel_candidate(n):
    """Check if a number is a Lychrel candidate."""
    results = []
    max_iterations = 10001
    max_length = 15000

    for iterations in range(max_iterations):
        if is_palindrome(n):
            print("NO")
            print("\n".join(map(str, results)))
            return

        # Perform reverse-and-add operation
        n += reverse_number(n)
        results.append(n)

        # Check length
        if len(str(n)) >= max_length:
            print("YES")
            print(iterations + 1, n)
            return

    print("YES")
    print(max_iterations,"\n",n)

#
# # Example usage
# number = 196  # Change this number to test other cases
n = int(input().strip())
lychrel_candidate(n)
