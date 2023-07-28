from collections import deque

def solution(skill, skill_trees):
    cnt = 0

    for skill_tree in skill_trees:
        queue = deque(skill)

        for idx, check_skill in enumerate(skill_tree):
            if check_skill in skill and queue.popleft() != check_skill:
                break
            if idx + 1 == len(skill_tree):
                cnt += 1
    

    return cnt