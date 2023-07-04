# def solution(brown, yellow):
    
#     total = brown + yellow # 총 블럭 수
    
#     for a in range(1, total+1):
#         if total % a == 0: # 가로 또는 세로의 길이가 가능할 때
#             b = total // a
#             if b > a:
#                 a, b = b, a # 출력: 가로, 세로 순
#             if yellow == total - (2*a+2*b-4):
#                 return [a, b]