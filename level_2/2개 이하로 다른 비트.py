def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0: # 짝수
            answer.append(number + 1)
        else: # 홀수
            bin_number = list('0' + bin(number)[2:]) # 0~1 인덱스 : 0b
            idx = ''.join(bin_number).rfind('0')
            bin_number[idx] = '1'
            bin_number[idx+1] = '0'
            answer.append(int(''.join(bin_number), 2)) 

    return answer