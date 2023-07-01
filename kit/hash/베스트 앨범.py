# 입력 
# genres: ["classic", "pop", "classic", "classic", "pop"], plays: [500, 600, 150, 800, 2500])

'코드 진행'
# import heapq

# def solution(genres, plays):
#     genres_val_dict = {}
#     genre_heap = []

#     # 연산 후 해시에 저장
#     for i, (genre, play) in enumerate(zip(genres, plays)): 
#         if genre not in genres_val_dict:
#             genres_val_dict[genre] = (play, [(play, i)])

#         else:
#             total_play, play_list = genres_val_dict[genre]
#             total_play += play
#             play_list.append((play, i))
#             genres_val_dict[genre] = (total_play, play_list)

#     # 최대 힙 트리에 합계 저장 / 정렬
#     for genre, (total_play, play_list) in genres_val_dict.items():
#         heapq.heappush(genre_heap, (-total_play, genre))

#         play_list.sort(key=lambda x: (-x[0], x[1]))  
#         genres_val_dict[genre] = play_list

#     # 출력
#     answer = []
#     while genre_heap:
#         _, genre = heapq.heappop(genre_heap)
#         for _, i in genres_val_dict[genre][:2]:  
#             answer.append(i)

#     return answer

'최적화'
# import heapq

# def solution(genres, plays):
#     genres_val_dict = {}
#     genre_heap = []

#     # 연산 후 값 해시, 최대 힙 트리에 저장
#     for i, (genre, play) in enumerate(zip(genres, plays)): 
#         if genre not in genres_val_dict:
#             genres_val_dict[genre] = [play, [(-play, i)]]
#         else:
#             genres_val_dict[genre][0] += play
#             # 최대 힙 구조로 저장
#             heapq.heappush(genres_val_dict[genre][1], (-play, i))

#     # 다른 최대 힙에 장르 순서 저장
#     for genre, info in genres_val_dict.items():
#         heapq.heappush(genre_heap, (-info[0], genre))

#     # 출력
#     answer = []
#     while genre_heap:
#         _, genre = heapq.heappop(genre_heap)
#         for _ in range(2):
#             if genres_val_dict[genre][1]:
#                 _, i = heapq.heappop(genres_val_dict[genre][1])
#                 answer.append(i)
                
#     return answer