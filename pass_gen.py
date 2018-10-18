import random

# this script is not finished
# it works perfectly for strong and weak passwords but I had not the time to generate neither
# medium passwords neither to generate them in a nice fashion

base_l="abcdefghilmopqrstuvzxykwj"
base_L="ABCDEFGHILMOPQRSTUVZXYKWJ"
base_n="0123456789"
base_s="!£$%&/()=?^"
base_w="home land air spirit shark pardon goat wrap urgency mechanic log solo mutation fee election eye Sunday cigarette carrot wardrobe relief movie beard palm"
base_w=base_w.split()

base="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

level=str(input("Choose strenght of the password (strong, weak) :"))

lenght=10

i=0

if level == 'strong':
 pwd=random.sample(base,lenght)
 pwd="".join(pwd)
 print(pwd)
 
elif level == 'weak':
 pwd=random.sample(base_w,1)
 while i < lenght-1:
  s=str(random.sample(base,1))
  pwd.append(s)
  i=i+1
 pwd="".join(pwd)
 print(pwd)

else:
 print("Wrong choice! You must type strong or weak.")
