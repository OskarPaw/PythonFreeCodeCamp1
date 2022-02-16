print("Welcome to my first game!")
print("Are you ready to play?")

name = input("What is your name? ")
NameLength = len(name)
if NameLength <= 10:
    print(("Good luck on your adventur ") + name +(" !!!"))
elif NameLength >= 10:
    print("Your name is too long! (MAXIMUM IS 20 CHARACTERS)")
    name = input("What is your finnal name adventurer ? ")
    if len(name) <=10:
        print(("Good luck on your adventur ") + name +(" !!!"))

        
#age = int(input(f"What is your age {name} ? "))
while True:
    try:
        age = int(input(f"What is your age {name} ? ")) # if /elif/else prob
        if age in range(18 - 100):
            print("Thx for typing your correct age! ")
            break
        elif age not in range(18):
            print(age)
            print("Thx for typing your correct age! ")
            break
        else:
            if age not in range(100):
                # print(input("Type you're correct age please ! ;) "))
                print("Its not your correct age !! ")
                continue

        #correct_age = int(input("It's your last chance to type your correct age ;) "))
       # if age in range(18-100):
           # break
            #if correct_age in range(0-100):
                #break

    except ValueError:
        print("It's your last chance to type your correct age!! ")
        age = int(input("So what is your correct age ? "))
        print(f"So you are {age} years old , have fun during the game {name} ")
        if age in range(18-100):
            print(f"So you are {age} years old , have fun during the game {name} ")
        break
        if age not in range(18-100):
            continue


health = 10

if age >= 18:
#if correct_age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    if wants_to_play == "yes":
        print("You are staring with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ").lower()

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ").lower()
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")

            else:
                print("You fell in the river and lost...")


        else:
            print("You fell down and lost...")

    else:
        print("Cya...")
else:
    print("You are not old enough to play...")
