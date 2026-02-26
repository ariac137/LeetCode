class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        
        primes = [i for i in range(2, n)]

        for prime in primes:
            if prime * prime <= n:
                primes = [i for i in primes if (i == prime or i % prime != 0)]
            else:
                break
            
        return len(primes)