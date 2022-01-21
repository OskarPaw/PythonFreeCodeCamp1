
for i in range(10):
    print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "Oskar P":
    print(i)

import time

for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print("Szczęścliwego Nowego Roku")

rows= int(input("How many rows: "))
columns= int(input("How many columns?: "))
symbol= input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# Loop Control Statements =change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next interation of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-8790"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

phone_number2 = "123-456-9790"
for i in phone_number2:
    if i == "-":
        continue
    print(i)

for i in range(1,21):

    if i == 13:
        pass
    else:
        print(i)
