# Hàm DFS để duyệt từ một vị trí có trạm ga
def dfs(x, y, grid, visited):
    visited[x][y] = True
    # Các hướng di chuyển: lên, xuống, trái, phải
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 2 and 0 <= ny < 2 and not visited[nx][ny] and grid[nx][ny] == '#':
            dfs(nx, ny, grid, visited)


def check_connectivity(grid):
    visited = [[False for _ in range(2)] for _ in range(2)]

    # Tìm một thành phố có trạm ga đầu tiên
    found = False
    for i in range(2):
        for j in range(2):
            if grid[i][j] == '#':
                dfs(i, j, grid, visited)
                found = True
                break
        if found:
            break

    # Kiểm tra tất cả các thành phố có trạm ga đều được thăm
    for i in range(2):
        for j in range(2):
            if grid[i][j] == '#' and not visited[i][j]:
                return "No"
    return "Yes"


# Đọc input
grid = [input().strip() for _ in range(2)]

# Kiểm tra tính kết nối
result = check_connectivity(grid)
print(result)
