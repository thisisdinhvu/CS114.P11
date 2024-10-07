def reverse(x):
  n = 0
  while x > 0:
    n = n * 10 + x % 10
    x = x // 10
  return n

def isPalindrome(n):
  return reverse(n) == n

def lychrel_candidate(n):
    results = []
    max_iterations = 10001
    max_length = 15000
    for iterations in range(max_iterations):
        if isPalindrome(n):
            print("NO")
            print("\n".join(map(str, results)))
            return
        # Perform reverse-and-add operation
        n += reverse(n)
        results.append(n)
        # Check length
        if len(str(n)) >= max_length:
            print("YES")
            print(iterations + 1, n)
            return
    print("YES")
    print(max_iterations,"\n",n)

n = int(input().strip())
lychrel_candidate(n)