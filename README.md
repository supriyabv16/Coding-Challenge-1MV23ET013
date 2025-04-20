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


3.Vowel and Consonant counter (Medium) 
  def count_v_c(string):
    vowels='aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    for char in string:
         if char.isalpha():
           if char in vowels:
              vowel_count += 1
           else:
              consonant_count += 1
         return vowel_count, consonant_count
input_string = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(input_string)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")


4.Center-Aligned Star Triangle 
n=int(input("Enter the number of rows:"))
for i in range(0,n):
  for j in range(0,num-i-1):
     print(end="")
  for j in range(0,i+1):
     print("*", end="")
  print()   
     
   
      
