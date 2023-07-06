'완전 탐색'
# from collections import deque
# from itertools import product

# def solution(name):    
#     results = []
#     cnt = 0
#     for rs in product((-1,1), repeat=len(name)-1):
#         cnt+=1
#         print(rs)
#         name_deque = deque(name)
#         default = deque('A'*len(name))

#         for c, r in enumerate([0]+list(rs)):
#             default.rotate(r)
#             name_deque.rotate(r)
#             default[0] = name_deque[0]

#             if name_deque == default:
#                 results.append(c)
#                 break
#     print(cnt)
#     return min(set(results))+sum([min(ord(l)-ord('A'), ord('Z')-ord(l)+1) for l in name])

'규칙 확인 후, 완전 탐색'
# def solution(name):
#     answer = 0
    
#     num_list = [min( abs(ord('A')-ord(n)) , 26-abs(ord('A')-ord(n)) ) for n in name]
#     # 각 문자 위, 아래 최소 이동 횟수 모든 합
#     answer += sum(num_list)
#     min_move = len(name) - 1
    
#     for i, c in enumerate(name):
#         next_i = i+1
#         while next_i < len(name) and name[next_i] == 'A':
#             next_i += 1
#         # 1. 기존 이동 / 해당 문자열 위치에서의  다음 A문자열 2. 왼쪽에서 시작, 3.오른쪽에서 시작
#         # 1~3 값 중 최소값 업데이트 (가장 긴 A 반복 구간을 피하는 경우가 최소 수평 이동 횟수)
#         min_move = min(min_move, 2*i + len(name)-next_i, 2*(len(name)-next_i) + i)
    
#     return answer+min_move