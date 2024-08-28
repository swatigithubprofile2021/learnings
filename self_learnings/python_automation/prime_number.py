

# Python program to print all  
# prime number in an interval 
  
start = 1
end = 100
  
# loop through the numbers 
for num in range(start, end + 1): 
  
   # prime numbers are greater than 1
   if num > 1: 
       for i in range(2, num): 
           if (num % i) == 0: 
               break
       else: 
           print(num)