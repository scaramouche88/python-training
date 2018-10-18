import random

# definition of the game's rules

def game(p1, p2):
 if p1 == p2:
  r=0
  return r
 elif p1 == 'rock':
  if p2 == 'paper':
   r=2
   return r
  elif p2 == 'scissor':
   r=1
   return r
 elif p1 == 'paper':
  if p2 == 'rock':
   r=1
   return r
  elif p2 == 'scissor':
   r=2
   return r
 elif p1 == 'scissor':
  if p2 == 'rock':
   r=2
   return r
  elif p2 == 'paper':
   r=1
   return r

# this script makes the computer plays with itself the game "rock scissor paper"
# you can give the amount of plays and it returns the percentage of winning, failure and draws

a=int(input("Give me the total number of plays: "))

list=['rock','scissor','paper']

i=0
w1=0
w2=0
d=0
x=0

while i < a:

 p2=random.choice(list)
 p1=random.choice(list)

 x=game(p1,p2)

 if x == 0:
  d=d+1
 elif x == 1:
  w1=w1+1
 elif x == 2:
  w2=w2+1

 i=i+1

# when the game is finish, it prints the results in %

 if i == a:

  w1=(w1/a)*100
  w2=(w2/a)*100
  d=(d/a)*100

  print("Percentage of P1 wins: ", w1, "%")
  print("Percentage of P1 losses: ", w2, "%")
  print("Percentage of draws: ", d, "%")
  print("End game!") 
