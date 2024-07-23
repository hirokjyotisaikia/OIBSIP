import string
import random
import sys

if __name__ == "__main__":
    ascii = string.ascii_letters #many modes
    # print(ascii)

    ascii1 = string.ascii_lowercase
    # print(ascii1)

    ascii2 = string.ascii_uppercase
    # print(ascii2)

    ascii3 = string.digits
    # print(ascii3)

    ascii4 = string.punctuation
    # print(ascii4)

p_length = input("Enter the password length: \n") #length of the pasword

if p_length.isdigit(): #this will check if the user gave an integer inpuut or not
    p_length = int(p_length)
    print("Input accepted \n")
else:
    sys.exit("wrong input, please enter integers") #exits if it is not integer while showing the text

p = [] #empty list and extended all the ascii variables from 0-4 in the list
p.extend(list(ascii))
p.extend(list(ascii1))
p.extend(list(ascii2))
p.extend(list(ascii3))
p.extend(list(ascii4))
random.shuffle(p) #this shuffled all the string constraints which was extended to p
print("Your password is: ")
print("".join(p[0:p_length]))#prints the password with specific length
