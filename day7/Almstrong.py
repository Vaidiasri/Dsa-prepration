# Check if the number is Armstrong or not
def is_armstrong(n):
  original_n = n
  number_of_digits = len(str(n))
  total = 0
  while n > 0:
    last_digit = n % 10
    total += (last_digit ** number_of_digits)
    n //= 10
  return total == original_n

# Test the function
# print(is_armstrong(153)) # Should return True
# print(is_armstrong(9))   # Should return True
# print(is_armstrong(10))  # Should return False
