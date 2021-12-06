import sys

x = 2
print(x)

# x is a variable something I made
# print is a reserved word with discripted use
# operator +-=

width = 15
height = 12.0
print(height/3)

type(height)
# < less than
# <= Less than or Equal to
# == Equal to ?
# >= Greater than or Equal to
# > greater than
# != Not equal

# iteration variable is saying how many time a loop is going over and over again


n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")
print(n)

for i in [5, 4, 3, 2, 1]:
    print(i+2)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

#counting in a loop

zork = 0
print("Before",zork)
for numbers in [ 9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, numbers)
print("After", zork)

# summing in a loop

zor = 0
print("Before", zor)
for number in [9, 41, 12, 3, 74, 15] :
    zor = zor + number
    print(zor, number)
print("After", zor)

#finding the average in a loop

count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum/count)

#filteting in a loop
 # if something >=< number:

print("Before")
for valu in [9, 41, 12, 3, 74, 15] :
    if valu > 20:
        print("Larger number", valu)
print("After")

# Search using boolean variable
# The Python Boolean type has only two possible values: True/False

search = False
print("Before", search)
for val in [9, 41, 12, 3, 74, 15] :
    if val == 3:
        search = True
    print(search, val)
print("After", search)

# how to find the biggest value

largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:  # looking for a greater number (while holding recent largest one)
        largest_so_far = the_num  #grabbing value line
    print(largest_so_far, the_num)
print("After", largest_so_far)

# how to find smallest number

smallest_so_far = 100
print("Before", smallest_so_far)
for the_nu in [9, 41, 12, 3, 74, 15]:
    if the_nu < smallest_so_far:  # looking for a smaller number (while holding recent smallest one)
        smallest_so_far = the_nu  #grabbing value line
    print(smallest_so_far, the_nu)
print("After", smallest_so_far)

# how to find smallest number by using NONE/ we haven't seen any number so far
# it only holds nothing just a blank space

smalles = None
print("Before")
for val in [9, 41, 12, 3, 74, 15]:
    if smalles is None: #None is stronger than is
        smalles = val
    elif val < smalles:
        smalles = val
    print(smalles, val)
print("After", smalles)

# is/is not = is the same as/its not the same as, only useable on none or booleans( true or false)
# is 0 is 0.0 FALSE
# is 0 == 0.0 TRUE    == true is weaker form which is useable


nun = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    #print(sval)
    nun = nun + 1
    tot = tot + fval

#print("ALL DONE")
print(nun, tot, tot/nun)
