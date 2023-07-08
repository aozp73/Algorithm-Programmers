# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x: x[1])
#     camera_posi = -30001 

#     for route in routes:
#         if camera_posi < route[0]:
#             answer += 1
#             camera_posi = route[1]
#     return answer