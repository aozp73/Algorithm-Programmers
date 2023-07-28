def solution(dirs):
    
    # L R U D 
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    check_list = []
    x, y = 0, 0
    
    for dir in dirs:
        for i in range(len(move_types)):
            if dir == move_types[i]:
               nx = x + dx[i]
               ny = y + dy[i]
        
        if not -5 <= nx <= 5 or not -5 <= ny <= 5:
            continue
        
        if {(x, y), (nx, ny)} not in check_list:
            check_list.append({(x, y), (nx, ny)})

        x, y = nx, ny


    return len(check_list)

print(solution("ULURRDLLU"))