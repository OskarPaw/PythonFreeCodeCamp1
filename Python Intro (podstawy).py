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

#                                                                                READING FILES
# Opening a file is done by open() function
# We are using open() by : handle = open (filename,mode) for example fhand = open("mbox.txt", "r")
# handle is a variable which let us hold a file and manipulate it
# File name is a string
# Mode is optional. R if we are planning to read the file , "w" if we're going to write to the file

# NEWLINE IN FILES : \n
# It indicate when a line ends.
# Its a one character not two so if we used len command with \n in line its counted as one
xyz = "Hello\nThere!"
print(xyz)

# Counting Lines in a File
# Use a for loop to read each line
#fhand = open("mbox.txt")
#count = 0
#for line in fhand:
    #count = count + 1 # Count the lines and print out the number of lines
#print("Line Count: ", count)

# We can read the whole file into a single string
# fhand = open("mbox-short.txt")
# inp = fhand.read()
# print(len(inp)) #number of characters in file
# print(inp[:20]) # prints only 20 first characters not including last one (20)

# Searching Through a File
# we can put an if statement in our for loop to only print lines that meet some criteria
# the newline is considered as a white space and is stripped by rstrip() string from the right
# fhand = open("random-file.txt")
# for line in fhand:
#     line = line.rstrip()
#     if line.startswitch("our criteria") :
#          print(line)

# Skipping with continue
# we can conveniently skip a line by using the continue statement
# fhan = open("random-file-fame.txt")
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswitch("From: ") :
#         continue
#     print(line)

# Using in to select lines
# we can look for a string anywhere in a line as our selection criteria
# fhan = open("random-file-fame.txt")
# for line in fhand:
#     line = line.rstrip()
#     if not "Thanks for your reply" in line : # if words in "" are not it the line, line will get skipped
#          continue
#     print(line)

# Prompt for file name
# with try and except there wont be an error if someone misstype file name
# fname = input("Enter the file name: ")
# try:
#      fhand = open(fname)
# except:
#        print("File cannot be opened:", fname)
#        quit()
# count = 0
# for line in fhand:
#     if line.startswitch("Subject: ") :
#         count = count +1
# pirnt("There were", count, "subject lines in", fname)
# it allows us to change file which we wanna check without coping a code

#                                                                                   LISTS
# What is not a collection
# most of variables have one value in them - when we put a new value in the variable, the old value is overwritten
# x = 2
# x = 4
# print(x) # 4

# A List is a kind of Collection
# collection allows us to put many values in a single "variable"
# collection let us carry many values around in one convenient package
# friend = [ "Hans", "Oskar", "Rajesh"]
# a list element can be any Python object even another list

# Lists and definite loops - best friends
# x = ["Hans", "Oskar", "Rajesh"]
# for z in x:
#     print("Happy New Year:", z) # H N Y: H | # H N Y: O | # H N Y: R
# print("Done!") # Done!

# Looking inside lists
# just like strings, we can get at any single element in a list using an index specified in square brackets[]
# friends = ["Hans", "Oskar", "Rajesh"]
# print(friends[1]) # Oskar

# List are Mutable strings are Not
# string are immutable - we cannot change the contents of a string - we must make a new string to make changes in it
# fruit = "Banana"
# fruit[0] = "b" # error "str" object does not support item assignment
# x = fruit.lower() # were added a new variable x to modify it as we like
# print(x) #banana
# lists are mutable we can change an element of a list using the index[] operator
# random number = [1, 2, 3, 4, 5]
# print(random number) [1, 2, 3, 4, 5]
# random number[2] = 28
# print(random number) # [1, 2, 28, 4, 5]

# How long is list
# the len() function takes a list as a parameter and returns the number of in the list
# greet = "Hello Hans"
# print(len(greet)) #9 number of letters
# len() tells us the number of elements of any set or sequence (such as a string)
# x = [1, 2, "joe", 99]
# print(len(x)) # 4 number of elements

# Using the range function
# range function returns a list of numbers that range from zero to one less than parameter
# print(range(4)) # [0, 1, 2, 3]
# friends = ["Hans", "Oskar", "Rajesh"]
# print(len(friends)) #3
# We can use construct an index loop using or and an integer iterator( iterator jest obiektem, który definiuje sposób wykonywania iteracji)
# iteracja to proces pobierania jednego elementu na raz z rzędu elementów.
# print(range(len(friends))) # [0, 1, 2]

# 2 Loops way
# If you dont need the position of object in a loop
# friends = ["Hans", "Oskar", "Rajesh"]
# for friend in friends :
# print("Happy New Year:"), friend) # H N Y: H | # H N Y: O | # H N Y: R
# If you need the position of object in a loop without gaps
# for i in range (len(friends)):
#     friend = friends[i]
#     print("Happy New Year:", friend)

# We can concatenate lists by using +
# we create a new list by adding two existing lists together
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b

# Lists can be sliced using :
# t = [9, 41, 12, 3, 74, 15]
# t[1:3] # [41,12]
# t[0:3] # [9, 41, 12]
# t[:4] # [9 ,41, 12, 3]
# just like in strings, the second number is " up to but not including"

# Building a List from Scratch
# we can create an empty list and then add elements using the append method 
# the list stays in order and new elements are added at the end of the list
# stuff = list()
# stuff.append("book")
# stuff.append(99)
# print(stuff) # ["book", 99]
# stuff.append("rice")
# print(stuff) # ["book", 99, "rice"]

# Is something in a List?
# python have two operators that let us check if an item is in a list in /not in
# these are logical operators that return True or False they don't modify the list
# some = [1, 9, 21, 10, 16]
# 9 in some #True
# 15 in some #False
# 20 not in some # True

# List are in Order
# a list can hold many items and keep them in order until we  do something to change the order
# a list can be sorted - we can change its order
# the sort method (unlike in strings)means sort yourself
# friends = ["Oskar", "Hans", "Sally")
# friends.sort()
# print(friends)
# print(friends[1])

# Built-in Fuctions and Lists
# there are numbers of functions built into python that take lists as parameters
#nums = [3, 41, 12, 9, 74, 15]
#print(len(nums)) #6
#print(max(nums)) #74
#print(min(nums)) #3
#print(sum(nums)) #154
#print(sum(nums)/len(nums)) #25.666666666666668

# 2 Different ways to build loops to count max and min with functions by making lists
# Less memory usage way
# total = 0
# count = 0
# while True:
#   inp = input("Enter a number: ")
#   if inp == "done" : break
#   value = float(inp)
#   total = total + value
#   count = count + 1
# average = total / count
# print("Average:", average)
# More memory usage by creating a totaly new list by appending list
# numlist = list()
# while True:
#   inp = input("Enter a number: ")
#   if inp == "done" : break
#   value = float(inp)
#   numlist.append(value)
# average = sum(numlist) / len(numlist)
# print("Average", average)

#                                                                               Strings and Lists
# Split breaks a string into parts and produces a list of strings. We think of these as words.
# we can access a particular word or lopp through all the words
# abc = "With these words"
# stuff = abc.split()
# print(stuff) # ["With", "these", "words"]
# print(len(stuff)) # 3
# print(stuff[0]) # With
#  Split deletes all blank spaces no matter how big they are
# line = "A lot              of spaces"
# etc = line.split()
# print(etc) # ["A", "lot", "of", "spaces"]
# When you don't specify a delimiter, multiple spaces are treated like one delimiter
# you can specify what delimiter(ogranicznik) character to use in te splitting .split(";") for example
# without delimiter below it coudn't delete blank spaces couse there were none
# line = "first;second;third"
# thing = line.split()
# print(thing) # [first;second;third"]
# print(len(thing)) # 1
# With delimiter usage there is specification was we want to get rid of .split("smth we want to get rid of)")
# thing = line.split(";")
# print(thing) # ["first", "second", "third"]
# print(len(thing)) # 3

# The Double Split Pattern
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# words = line.split()
# email = words[1] #stephen.marquard@uct.ac.za
# pieces =  email.split("@") # ["stephen.marquard", "uct.ac.za"]
# print(pieces[1]) # "uct.ac.za"

#                           Python Dictionaries
# Dictionaries are like a bag with random stuff in it but they are labeled but they have no order
# lists are more organised than dictionaries
# we index the things we put in the dictionary with a "lookup tag"
# purse = dict()
# purse["money"] = 12 #money is a label
# purse["candy"] = 3 # candy is a label
# purse["tissues"] = 75 # tissues is a label
# print(purse) #{'money': 12, 'candy': 3, 'tissues': 75} # random order
# print(purse["candy"]) # 3 # we can ask by using index operator[""] about what is in candy
# print(purse["candy"]) = purse["candy"] + 2 # we can update stuff
# print(purse) # {'money': 12, 'candy': 5, 'tissues': 75}
# if we have some values like dict = {"Fri": 20, "Thu": 6, "Sat": 1} we can overwrite them by simply doing dict["Sat"] = 2

# Dictionary literals(Constants)
# dictionary literals use curly braces and have a list of key: value pairs
# jjj = { "chuck" : 1, "fred" : 4}
# print(jjj) # { "chuck" : 1, "fred" : 4}
# you can make an empty dictionary using empty curly braces
# ooo = { }
# print{ooo} # {}

# Comparing Lists and Dictionaries
# lst = list()                         ddd = dict()
# lst.append(2)                        ddd["age"] = 2
# lst.append(180)                      ddd("course"] = 180
# print(lst) # [2, 180]                print(ddd) # {course": 180, "age": 2)
# lst[0] = 24                          ddd["age"] = 24
# print(lst) # [ 24, 180]              print(ddd) # {course": 180, "age": 24}

# When there is a new name in dictionary we need to add a new entry in a the dictionary
# if this the second or later time we have seen the name we simply add one to the count in the dict under the name
# counts = dict()
# names = ["A", "B","C","A","B"]
# for name in names:
#   if name not in counts:
#        counts[name] = 1
#    else:
#       counts[name] = counts[name]+ 1
# print(counts)

# The get method for dictionaries
# method .get() the pattern of checking to see if a key is already in dict and assuming a deafult value
# if the key is not there .
# we can just simply type x = counts.get(name, 0)
# instead of :
# if name in counts:
#    x = counts[name]
# else:
#     x = 0

#                               Counting words in Text
# Counting pattern - general pattern to count the words in a line of text is to split the line into words,
# then loop through them and use a dictionary to track the count of each word independently
# # even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in dictionary
# counts = dict()
# print("Enter a line of text:") # the clown ran after the car and the car ran into the tent and the tent fell down
# line = input("")
# words = line.split()
# print("Words:", words) # ['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 'ran', 'into', 'the', 'tent', 'and', 'the', 'tent', 'fell', 'down']
# for word in words:
#    counts[word] = counts.get(word, 0) + 1
# print("Counts", counts) #{'the': 5, 'clown': 1, 'ran': 2, 'after': 1, 'car': 2, 'and': 2, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1}

# Retrieving lists of Keys and Values
# you can get a list of keys, values, or items(both) from dictionary
# jjj = {"Hans": 1, "Fred": 42, "Himmler": 100}
# print(list(jjj)) # ['Hans', 'Fred', 'Himmler']
# print(jjj.keys()) # dict_keys(['Hans', 'Fred', 'Himmler'])
# print(jjj.values()) # dict_values([1, 42, 100])
# print(jjj.items()) # dict_items([('Hans', 1), ('Fred', 42), ('Himmler', 100)])

# Two Iteration Variables
# we loop through the key- value pairs ( { "Hans": 1} in a dictionary using "two" iteration variables
# ech iteration, the first variable is the key and the second variable is the corresponding value fot tke key
# jjj = {"Hans": 1, "Himmler": 100, "Fred": 42}
# for a,b in jjj.items():
#     print(a,b)
# Hans 1
# Himmler 100
# Fred 42
