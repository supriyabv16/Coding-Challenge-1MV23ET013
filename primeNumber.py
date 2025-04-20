N=int(input("Enter the max value:"))
for N in range(1,N+1):
  count=0
  for i in range(2,(N//2+1)):
     if(N%i==0):
         count=count+1
         break

if(count==0 and N!=1):
   print("%d" %N, end='')
