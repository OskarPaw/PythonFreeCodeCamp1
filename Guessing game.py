import random
random_number = random.randint(1,25)
guessing = 0
count = 1

while guessing != random_number  and count <6:
    guessing = int(input("Make a guess between 1 - 25: "))
    if (guessing > random_number):
        print("to high")
        count += 1
    elif ( guessing< random_number):
        print(" to low")
        count += 1
    #else:
        #print("Nice one, you've guessed it !")

if(count<6):
    print(f"Wow ,you've made it after {count} guesses! ")
else:
    print("Sadly you've run out of guesses")
