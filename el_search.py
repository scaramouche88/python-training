import random

# normal and binary search for a randomnly generated list of numbers

#######################

# normal search

def search(test,n):
 for i in test:
  if i == n:
   return True
 return False

#######################

# binary search

def bin_search(test,n):
 start_i=0
 end_i=len(test)-1
 max=test[end_i]
 
# the next two lines are just to avoid the search in case the number is too high
 
 if n > max:
  return False 
 
 while start_i <= end_i:

  middle_i=int((end_i-start_i)/2)
  middle_i=middle_i+start_i

# as an alternative for the above division, one can use (end_i-start_i)//2
  
  middle_n=test[middle_i]  
  
# this print line, now commented, is to verify which steps the binary search takes  
# print("Start ", start_i," End ", end_i," middle ", middle_i," value of middle ", middle_n)

# the next if cycle is to avoid oscillations when the search is on lenght of 2

  if end_i-start_i <= 1:
   if end_i == n:
    return True
   elif start_i == n:
    return True
   return False 
 
  if middle_n < n:
   start_i=middle_i
  elif middle_n > n:
   end_i=middle_i
  else:
   return True
  
 return False

#######################

# ask for the number to be searched

print("Which number do you want to search?")
numb=int(input())

# this generate a random list of ordered numbers with max lenght of 30

list_max=random.randint(5,30)
list=random.sample(range(30),list_max)
list.sort()

# call the search function

ans1=search(list,numb)
ans2=bin_search(list,numb)

print("Result of the normal search:")
print(ans1)
print("Result of the binary search:")
print(ans2)
print("Original list:")
print(list)

