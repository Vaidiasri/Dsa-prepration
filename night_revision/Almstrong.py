num=153
lenght=len(str(num))
def Alm(num,lenght):
  original_num = num  # Save the original value
  result = 0
  while num > 0:
    rem = num % 10
    result = result + rem**lenght
    num = num // 10
  if result == original_num:  # Compare with original
    return "Armstrong"
  else:
    return "not Armstrong"
print(Alm(num,lenght))