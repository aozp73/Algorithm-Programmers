from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()

        for menu_combination, count in most_ordered:
            if count > 1 and count == most_ordered[0][1]:
                    result.append(''.join(menu_combination))

    return sorted(result)


