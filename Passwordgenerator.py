import random
import string
print("--------PASSWORD GENERATOR------------")
print()
length=int(input("ENTER THE LENGH OF PASSWORD:"))
characters=string.ascii_letters+string.digits
password=" "
for i in range(length):
    password+=random.choice(characters)
print("GENERATED PASSWORD:",password)
