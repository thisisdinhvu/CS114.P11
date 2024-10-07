def is_palindrome_str_optimized(s):
    """Kiểm tra xem chuỗi số có phải palindrome bằng cách so sánh từ hai đầu."""
    return s == s[::-1]

def reverse_and_add(n):
    """Thực hiện thao tác reverse-and-add."""
    reversed_n = int(str(n)[::-1])
    return n + reversed_n

def lychrel_candidate(n):
    try:
        iterations = 0
        current = n

        # Thực hiện tối đa 10,000 lần lặp hoặc đến khi số có độ dài vượt quá 15,000 chữ số
        while iterations < 10000 and len(str(current)) < 15000:
            current_str = str(current)

            if is_palindrome_str_optimized(current_str):
                print("NO")
                print(n)
                print(current)
                return

            current = reverse_and_add(current)
            iterations += 1

        print("YES")
        print(iterations)
        print(current)

    except Exception as e:
        print(f"Runtime Error: {e}")

# Nhận input
if __name__ == "__main__":
    try:
        n = int(input().strip())  # Đọc số nguyên từ đầu vào
        lychrel_candidate(n)
    except Exception as e:
        print(f"Input Error: {e}")
