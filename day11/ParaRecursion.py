def  fun(sum,i,n):
  if (i>n):
    print(sum)
    return
  fun(sum+i,i+1,n)
fun(0,1,15)