# import heapq

# def solution(jobs):
#     jobs = sorted(jobs, key=lambda x: x[0])
#     heap = []

#     end_time = 0
#     avg_data = []

#     while jobs or heap:
#         # 현재 시간 내에 요청되는 모든 작업들을 힙에 추가
#         while jobs and jobs[0][0] <= end_time:
#             req_time, job = jobs.pop(0)
#             heapq.heappush(heap, (job, req_time))

#         if heap:
#             job, req_time = heapq.heappop(heap)
#             end_time += job
#             avg_data.append(end_time - req_time)
#         else:
#             # 현재 처리할 수 있는 작업이 없다면, 다음 작업이 요청되는 시간으로 현재 시간 업데이트
#             if jobs:
#                 end_time = jobs[0][0]

#     res = sum(avg_data) // len(avg_data)

#     return res