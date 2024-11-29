from collections import deque




def BFS(x,y):
    queue = deque([x,y])
    farm[y][x] = 0
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            
            if 0<= nx < m and 0 <= ny < n and farm[ny][nx] == 1:
                farm[ny][nx] = 0
                queue.append((nx, ny))