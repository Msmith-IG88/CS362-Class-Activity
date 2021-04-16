def findDivisors(num):
    i = 1
    n = 0
    while i < (num / 2+1):
        if num % i == 0:
            n = n + 1
            print(i)
        i = i + 1
    print(str(num) + " has " + str(n) + " divisors")

def main():
    num = int(input("Enter Number: "))
    findDivisors(num)

main()