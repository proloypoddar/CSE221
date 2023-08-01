def dfs(grid, r, c, visited):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '#' or visited[r][c]:
        return 0
    visited[r][c] = True
    diamonds = 0
    if grid[r][c] == 'D':
        diamonds = 1
    u = dfs(grid, r - 1, c, visited)
    d = dfs(grid, r + 1, c, visited)
    l = dfs(grid, r, c - 1, visited)
    r = dfs(grid, r, c + 1, visited)
    return diamonds + max(u, d, l, r)
def dimond(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    m_dimond = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c] and grid[r][c] == '.':
                m_dimond = max(m_dimond, dfs(grid, r, c, visited))
    return m_dimond
def flood_fill():
    input_file_path = "F:/CSE221/LAB/LAB4/input_task6.txt"
    output_file_path = "F:/CSE221/LAB/LAB4/output_task6.txt"
    with open(input_file_path, "r") as file:
        R, H = map(int, file.readline().split())
        grid = [file.readline().strip() for i in range(R)]
    m_dimond = dimond(grid)
    with open(output_file_path, "w") as output_file:
        output_file.write(str(m_dimond))
flood_fill()
