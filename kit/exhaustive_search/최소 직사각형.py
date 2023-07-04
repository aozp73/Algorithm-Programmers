# def solution(sizes):
#     max_val1 = -int(1e9) 
#     max_val2 = -int(1e9)  
    
#     for size in sizes:
#         size.sort()
#         max_val1 = max(max_val1, size[0])
#         max_val2 = max(max_val2, size[1])
        
#     return max_val1 * max_val2

# print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)