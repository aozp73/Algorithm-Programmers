'조건, 과정에 따라 직접 구현'
# def solution(files):
#     s_files_list = []

#     for file in files:
#         s_temp = ()
#         work_check = 0  # 0: HEAD 작업, 1: NUMBER 작업
#         HEAD_idx_check = 0
#         NUMBER_idx_check = 0
#         s_head = ''
#         s_number = ''
#         s_tail = ''

#         for idx in range(len(file)):
#             if work_check == 0 and file[idx].isdigit():
#                 HEAD_idx_check = idx
#                 s_head = file[:HEAD_idx_check]
#                 work_check = 1

#             if work_check == 1 and not file[idx].isdigit():
#                 NUMBER_idx_check = idx
#                 s_number = file[HEAD_idx_check:NUMBER_idx_check]
#                 break
#             elif work_check == 1 and idx == len(file) - 1:
#                 NUMBER_idx_check = idx + 1
#                 s_number = file[HEAD_idx_check:NUMBER_idx_check]

#         s_tail = file[NUMBER_idx_check:]

#         s_temp = (s_head, s_number, s_tail)
#         s_files_list.append(s_temp)

#     s_files_list.sort(key=lambda x: (x[0].lower(), int(x[1])))

#     return ["".join(x) for x in s_files_list]


# print(solution(["foo010bar020.zip", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14"]))

're 모듈을 활용한 정규표현식 활용'
# import re

# def solution(files):
#     # 먼저, 각 파일 이름에서 숫자 부분을 찾아 첫번째 숫자 값 기준으로 오름차순 정렬
#     a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
#     print(a)
#     # 숫자로 분할된 첫 번째 문자열을 기준으로 정렬
#     # 여기서 문자열을 소문자로 변환하여 대소문자를 무시한 채로 비교하게 됨
#     b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
#     print(b)
#     return b

# print(solution(["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"] ))
