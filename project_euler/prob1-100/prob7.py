#URl - https://projecteuler.net/problem=7

#https://codereview.stackexchange.com/questions/188053/project-euler-problem-7-in-python-10001st-prime-number/188063

#https://math.stackexchange.com/questions/1270814/bounds-for-n-th-prime

#https://www.geeksforgeeks.org/prime-numbers/

#2,3,5
# i = 1
# while(i <= 9999 ):
#     num = 6*i + 1
#     i += 1

def isPrime(n, curr_prime_arr):
    for i in curr_prime_arr:
        if(n % i is 0):
            return False
    return True
