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

 # STRINGS
name = input("Enter your name :")
print("Your nick is :" + name)

apple = input("Enter amount of apples :")

#x = apple - 10
#Traceback (most recent call last):
# line 155, in <module>
    #x = apple - 10
#TypeError: unsupported operand type(s) for -: 'str' and 'int'

# Raw input numbers must be converted from strings by int /float
x = int(apple) - 10
print(x)

#           LOOKING INSIDE STRINGS

fruit = "banana"
letter = fruit[1] # square bracket chooses a letter in our string ( b-0, a-1, n-2, a-3 etc)
print(letter) #a
x = 3
w = fruit[x - 1]
print(w) #n

#               GETTING LENGHT IN STRINGS

frui = "banana"
print(len(frui)) # 6

#               LEN FUNCTION
frui = "banana"
x = len(frui)
print(x) #6

# banana ( a string input) ----> len(function) ----> 6 (a number output)
# a function is some stored code. A function takes some input and produces an output.

#              LOOPING THROUGH STRINGS
# by while statement and an iteration variable and the len function, we can construct
# a loop to look at each of the letters in a string individually

fru = "banana"
index = 0
while index < len(fru): # from 0 to 5 couse lenght of word banana is 6
    letter = fru[index] # taking letters from word banana
    print(index, letter)
    index = index + 1 # counting positions

#for loop if you dont need counting

fruit = "banana"
for letter in fruit:
    print(letter)

#               LOOPING AND COUNTING STRINGS
word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count +1
print(count)

#               SLICING STRINGS
#  second number is beyond the end of the slice - ###Up to but not including

s = "Monty Python"
print(s[0:4])
print(s[4:7])
print(s[7:20])
print(s[:2]) # if we leave off the first number or the last number of the slice
print(s[8:]) # its assumed to be the beginning or end of the string
print(s[:])

#               STRING CONCATENATION/ Łączenie stringów

# when + operator is applied to strings it means concatenation
a = "Hello"
b = a + "There"
print(b) #HelloThere

c = a + " " + "There"
print(c) #Hello There

#               USING IN AS A LOGICAL OPERATOR STRING
# The in expression is a logical expression that returns True or False and can be used in an if statement
# The in keyword can also be used to check to see if one string is "in" another string

fruit = "banana"
#"n" in fruit
#"m" in fruit
#"nan" in fruit
if "a" in fruit:
    print("Just found A!")

#                   STRING LIBRARY
# there is a number of string functions which are in the string library
# these functions are already built into every string - we invoke them by appending the funcion
# to the string variabe for example : .lower

print("Hi There" .lower()) #hi there

# These functions do not modify the original string, instead they give us a new string which was changed

greet = "Hello Hans"
zap = greet.lower()
print(zap) #hello hans
print(greet) #Hello Hans

# https://docs.python.org/3/library/stdtypes.html#string-methods all the string fuctions which are built in

                    #SEARCHING A STRING
# find() finds the first occurrence of the substring.String position starts at zero
# if the substring is not fond , find() returns -1

fruit = "banana"
pos = fruit.find("na")
print(pos) # 2

aa = fruit.find("z")
print(aa) # -1 due to not being able to find z letter

#               MAKE EVERYTHING UPPER CASE STRINGS
# you can make a copy of a string in lowe case or upper case

greet = "Hello Hans"
nnn = greet.upper()
print(nnn)#HELLO HANS

www = greet.lower()
print(www)#hello hans

#                           SEARCH AND REPLACE STRINGS
# the replace() function is search and replace operation
# it replaces all occurrences of the search string with the replacement string
greet = "Hello  Bob"
nstr = greet.replace("Bob", "Hans")
print(nstr) #Hello Hans

nstr = greet.replace("o","x")
print(nstr)# Hellx Bxb

#               STRIPPING WHITESPACE
#lstrip() and rstrip() remove whitespace at the left or right
#strip() removes both beginning and ending whitespace
greet = "   Hello Bob   "
greet.lstrip()  #"Hello Bob     "
greet.rstrip()   #"   Hello Bob"
greet.strip()   #"Hello Bob"

#               PREFIXES STRINGS

line = "Please have a nice day"
line.startswith("Please") #True
line.startswith("p") #False

#               Parsing and Extracting
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos) #21

sppos = data.find(" ", atpos) #lk for a blank space
print(sppos)#31

host = data[atpos+1 : sppos]
print(host) #uct.ac.za
