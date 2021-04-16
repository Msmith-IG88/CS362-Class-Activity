import random
import string

def randomPassword(num):
    characters = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(characters) for i in range(num))
    print("A password of length " + str(num) + " could be: " + result)

def main():
    num = input("Enter a password length: ")
    randomPassword(num)

main()