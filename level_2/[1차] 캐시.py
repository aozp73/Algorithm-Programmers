def solution(cacheSize, cities):
    
    s_cnt = 0
    s_cache = []
    
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        city = city.upper() # 문제조건 (대소문자 구분 x)
        
        if city in s_cache: # 캐시 메모리에 해당 데이터가 있는 경우 (캐시 히트)
            s_cnt += 1
            s_cache.remove(city)
            s_cache.append(city) # LRU 알고리즘
        else:  # 캐시 메모리에 해당 데이터가 없는 경우 (캐시 히트)
            s_cnt += 5
            if len(s_cache) < cacheSize:  # 캐시 메모리 공간이 있을 경우
                s_cache.append(city)
            else: # 캐시에 공간이 없을 경우
                s_cache.pop(0) # LRU 알고리즘
                s_cache.append(city)

    return s_cnt