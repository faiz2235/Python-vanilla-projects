import random

# PC number choose
Number = random.randint(1 , 99)
# Human guess
guess = int(input("What's your guess...??? "))

# repeat process
while guess != Number :
    if guess > Number :
       print ("try smaller !")
    elif guess < Number :
        print ("try bigger !")
    guess = int(input("What's your guess...??? "))
# win message
print ("You did it...")

print ("The number was " , Number)