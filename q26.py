from math import sqrt


def test_prime(n):
    if n==1 :
        return False
    elif n==2 :
        return True
    else:
        limit = int(sqrt(n))
        for i in range(2, limit):
            if n%i == 0:
                return False
            else:
                return True

def generate_prime(num):
    temp = []
    i=2
    while len(temp)<num:
        if test_prime(i):
            temp.append(i)
        i+=1
    return temp

num = int(input('How many prime numbers do you want : '))
result = generate_prime(num)
print(result)
