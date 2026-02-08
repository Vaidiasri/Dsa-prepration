#  Check the number is palindrome or not
n = 123
num = n
result = 0
while num > 0:
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10

if n == result:
    print("Palindrome")
else:
    print("Not a Palindrome")
