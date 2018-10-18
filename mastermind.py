import random
from numpy.random import randint

# the function verifies how many "cows" and "bulls" are there
# since functions cannot return lists, it returns two values that are merged into a list afterwards

def mastermind(number,guess):
 for i in range(len(number)):
  place_count=0
  right_count=0
  for i in range(len(number)):
   if guess[i] in number:
    right_count+=1
   if guess[i] == number[i]:
    place_count+=1
 return place_count,right_count

list_number=[0,1,2,3,4,5,6,7,8,9]

number=random.sample(list_number,4)

#print("The solution is:")
#print(number)

print("WELCOME TO MASTERMIND - by G.F.G.\n")

print("Give me four number as your guess (NOT separated by spaces): ")
guess = [int(x) for x in str(input())]

# the next 3 lines are redundant with those at the end - to be improved

if len(number)!=len(guess):
 print("You have not understood the rules of the game: you need to guess FOUR numbers!")
 exit()

max_test=9
test=1

while test<=max_test:
 
 print("This is your attempt N.", test," out of 9!")
 print("With your guess:")
 print(guess)
 count=mastermind(number,guess)
 place_count=count[0]
 right_count=count[1]

 if place_count == 4:
  print("You WON! The numbers are: ", number)
  exit()

 else:
  print("You have ", right_count," numbers RIGHT")
  print("You have ", place_count," numbers RIGHT in the RIGHT place \n") 
  test+=1
  if test==max_test+1:
   print("Sorry! You lost!")
   print("By the way the solution was: ", number)
   print("Bye!")
   exit()

  print("Give me four number as your guess (NOT separated by spaces): ")
  guess = [int(x) for x in str(input())]
  if len(number)!=len(guess):
   print("You have not understood the rules of the game: you need to guess FOUR numbers!")
   exit()





