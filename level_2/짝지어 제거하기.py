def solution(s):
    stack = []

    for char in s:
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # 스택 이 비어있다면 모든 짝을 다 맞춘 것이므로 1 리턴
    return 1 if not stack else 0