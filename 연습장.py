def make_prime_list(n):
    sieve = [False, False] + [True] * (n - 1)
    
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == False:
            continue
        
        for j in range(i + i, n + 1, i):
            sieve[j] = False