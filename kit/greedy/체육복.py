'단순 확인'
# def solution(n, lost, reserve):
    
#     stu_state = [1] * (n + 1)
#     for l in lost:
#         stu_state[l] -= 1
#     for r in reserve:
#         stu_state[r] += 1
    
#     lost_numbers = []
#     reserver_num = []
#     for i in range(1, n + 1):
#         if stu_state[i] == 0:
#             lost_numbers.append(i)
#         if stu_state[i] == 2:
#             reserver_num.append(i)
            
#     cnt = len(reserver_num)
#     if 1 in lost_numbers and 2 in reserver_num:
#         lost_numbers.remove(1)
#         reserver_num.remove(2)
#         cnt += 1
    
#     for lost_number in lost_numbers:
#         if lost_number + 1 in reserver_num:
#             lost_numbers.remove(lost_number)
#             reserver_num.remove(lost_number + 1)
#             cnt += 1
            
#         if lost_number - 1 in reserver_num:
#             lost_numbers.remove(lost_number)
#             reserver_num.remove(lost_number - 1)
#             cnt += 1

#     return cnt

'리프리헨션'
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)