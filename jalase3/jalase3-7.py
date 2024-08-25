# checks if the number is prime.
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        print(i)
        if n % i == 0:
            return False
        
    return True

x = input("Enter a number: ")

print(is_prime(int(x)))