num=121
def palin(num):
  original_num = num  # Save the original value
  result = 0
  while num > 0:
    rem = num % 10
    result = result * 10 + rem
    num = num // 10
  if result == original_num:  # Compare with original
    return "palindrome"
  else:
    return "not palindrome"
print(palin(num))