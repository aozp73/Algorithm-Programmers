'sor() 정렬 기준 명시'
# def solution(numbers):
    
#     numbers_str = list(map(str, numbers))                 
#     numbers_str.sort(key=lambda num: num*3, reverse=True)      
#     return str(int(''.join(numbers_str)))

# import functools

'정렬 함수 구현'
# def comparator(a,b):
#     t1 = a+b
#     t2 = b+a
#     #  t1이 크다면 1, t2가 크다면 -1,  같으면 0
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) 

# def solution(numbers):
#     n = [str(x) for x in numbers]
#     n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
#     answer = str(int(''.join(n)))
#     return answer