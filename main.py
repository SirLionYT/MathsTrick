import time


name = input("Hello, what is your name?\n")

time.sleep(2)
print("Hello " + name,)

time.sleep(2)
feeling = input("How are you today?\n")

time.sleep(3)
if feeling in ["Good", "good"]:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")


time.sleep(3)
question = input ("Would you like to play a quick Maths game?\n")

time.sleep(2)
if question in ["Yes", "yes"]:
    print("Okay, let's move on...")
else:
    print("Okay, it's fine!")

time.sleep(2)
game1 = input ("Pick a whole number between 1 to 10.\n")

time.sleep(3)
if game1 in [str(a) for a in range(1,10)]:
    print("Your number is:", game1)
else:
    print("Type a number between 1 to 10 please.")

time.sleep(5)
print ("Add 2")

time.sleep(5)
print ("Multiply by 2")

time.sleep(5)
print ("Subtract 2")

time.sleep(5)
print ("Divide it by 2")

time.sleep(5)
print ("Subtract your original number")


time.sleep(6)
answer = input ("Your final answer should be 1, am I right?\n")

time.sleep(2)
if answer in ["Yes", "yes"]:
   print("It was nice playing with you!")
else:
   print("There is no way!")