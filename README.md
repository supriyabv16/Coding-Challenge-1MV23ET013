# Coding-Challenge-1MV23ET013

1.Fibonacci series
  n=int(input("Enter the length of fibonacci series:"))
  a=0
  b=1
  print("The fibonacci series is:")
  print(a)
  print(b)
  for i in range(2,n):
      c=a+b
      print(c)
      a=b
      b=c

  2. prime numbers till N
  N=int(input("Enter the max value:"))
  for N in range(1,N+1):
     count=0
     for i in range(2,(N//2+1)):
        if(N%i==0):
            count=count+1
            break

    if(count==0 and N!=1):
         print("%d" %N, end='')


   3.      
   
      
