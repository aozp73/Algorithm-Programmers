'1. 반복문'
# 슬라이싱
# def solution(phone_book):
#     phone_book.sort()
    
#     for i in range(len(phone_book) - 1):
#         if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
#             return False
#     return True

# startswith
# def solution(phone_book):
#     phone_book.sort()
    
#     for i in range(len(phone_book) - 1):
#         if phone_book[i + 1].startswith(phone_book[i]):
#             return False
#     return True

'2. 해시'
# def solution(phone_book):
#     phone_book_hash = {}
    
#     for phone in phone_book:
#         phone_book_hash[phone] = 1
        
#     for phone in phone_book:
#         check_num = ""
#         for num in phone:
#             check_num += num
            
#             if check_num in phone_book_hash and check_num != phone:
#                 return False
    
#     return True