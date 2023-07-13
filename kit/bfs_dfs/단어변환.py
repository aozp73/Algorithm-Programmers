from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0

    word_length = len(begin)
    
    def can_change(word, change_word):
        cnt = 0
        for i in range(word_length):
            if word[i] != change_word[i]:
                cnt += 1
        if cnt == 1:
            return True
        else:
            return False
        
    def bfs():
        queue = deque([(begin, 0)])
        
        while queue:
            word, depth = queue.popleft()
            
            for change_word in words:
                if can_change(word, change_word):
                    words.remove(change_word)
                    if change_word == target:
                        return depth + 1
                    else:
                        queue.append([change_word, depth + 1])
        
        return 0

    return bfs()