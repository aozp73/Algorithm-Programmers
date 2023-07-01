'변수 활용'
# from math import ceil

# def solution(progresses, speeds):
#     answer = []
#     data = []
#     for progress, speed in zip(progresses, speeds):
#         data.append(ceil((100 - progress)/speed))
    
#     cnt = 1
#     max_dev_time = data[0]
#     for i in range(1, len(data)):
#         if max_dev_time >= data[i]:
#             cnt += 1
#         else:   
#             answer.append(cnt)
#             max_dev_time = data[i]
#             cnt = 1
#     answer.append(cnt)        
    
#     return answer

'스택 자료구조 활용'
# def solution(progresses, speeds):
#     Q=[]  
#     for p, s in zip(progresses, speeds):  
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s): # ﻿-((p-100) // s) : 올림 처리 
#             Q.append([-((p-100)//s),1])
#         else:  
#             Q[-1][1]+=1

#     return [q[1] for q in Q]