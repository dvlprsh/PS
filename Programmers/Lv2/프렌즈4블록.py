# Solve
# 풀이 1 - 정확성 100
def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    r_board = [[None] * m for _ in range(n)]
    
    for y in range(m):
        for x in range(n):
            r_board[x][m-1-y] = board[y][x]
    
    while True:
        garbage = set()
        for y in range(len(r_board)-1):
            for x in range(len(r_board[y])-1):
                try:
                    current = r_board[y][x]
                    n1 = r_board[y+1][x]
                    n2 = r_board[y][x+1]
                    n3 = r_board[y+1][x+1]  
                except:
                    continue
                if current == n1 and n1 == n2 and n2 == n3:
                    garbage.update([(y, x), (y+1, x), (y, x+1), (y+1, x+1)])    
                    
        if len(garbage) == 0:
            break
    
        for v in garbage:
            r_board[v[0]][v[1]] = 0
            
        answer += len(garbage)
        r_board = [list(filter(lambda x: x != 0, row)) for row in r_board]
    return answer

# 풀이 2 - 정확성 90.9
def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    r_board = [[None] * m for _ in range(n)]
 
    for y in range(m):
        for x in range(n):
            r_board[x][m-1-y] = board[y][x]
  
    while True:
        garbage = set()
        for y in range(n):
            for x in range(m):
                try:
                    current = r_board[y][x]
                    n1 = r_board[y+1][x]
                    n2 = r_board[y][x+1]
                    n3 = r_board[y+1][x+1]
                    if current == n1 and n1 == n2 and n2 == n3:
                        garbage.update([(y, x), (y+1, x), (y, x+1), (y+1, x+1)])
                except:
                    continue
                    
        if len(garbage) == 0:
            break
    
        for v in garbage:
            r_board[v[0]][v[1]] = 0
            
        answer += len(garbage)
        r_board = list(filter(lambda x: len(x) != 0, [list(filter(lambda x: x != 0, row)) for row in r_board]))
      
    return answer
# 풀이 3 - 정확성 81
def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    r_board = [[None] * m for _ in range(n)]
 
    for y in range(m):
        for x in range(n):
            r_board[x][m-1-y] = board[y][x]
    while True:
        # garbage item - (row, column, value)
        garbage = set()
        for y in range(len(r_board)):
            for x in range(m):
                try:
                    current = r_board[y][x]
                    n1 = r_board[y+1][x]
                    n2 = r_board[y][x+1]
                    n3 = r_board[y+1][x+1]
                    if current == n1 and n1 == n2 and n2 == n3:
                        garbage.update([(y, x, current), (y+1, x, n1), (y, x+1, n2), (y+1, x+1, n3)])
                except:
                    continue
        if len(garbage) == 0:
            break
    
        for v in garbage:
            r_board[v[0]].remove(v[2])
        answer += len(garbage)
        r_board = list(filter(lambda x: x != [], r_board))
    return answer