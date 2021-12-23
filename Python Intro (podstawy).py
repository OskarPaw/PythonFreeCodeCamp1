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

#                                                                                   READING FILES
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

#                                                                                              LISTS
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

#                                                                                    Python Dictionaries
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

#                                                                   Counting words in Text
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

#                                                                                   Tuples
# Tuples are another kind of sequence that function much like a list
# they have elements which are indexed starting at 0 , we use () instead of {}
# x = ("Hans", "Himmler", "Fred")
# print(x[2]) # Fred
# y = (1, 8, 2)
# print(y) #(1, 8, 2)
# print(max(y)) # 8
# for inter in y:
#    print(inter) # 1| 8| 2|

# Tuples are immutable /unchangeable
# Unlike a list, once you create a tuple, you cannot alter it content - similar to a string
# z = (5, 2, 1)
# z[2] = 0
# TypeError: 'tuple' object does not support item assignment
# in str there is same stuff
# y = "ABC"
# y[2] = "D"
# TypeError: 'str' object does not support item assignment

# Thing not to do with tuples
# x = (3, 2, 1)
# x.sort() you can't sort it
# x.append(5) you can't add things to tuple
# x.reverse() you can't flip the order

# Tuples are limited lists
# we can use count , index on them
# we use tuple when we wanna make a temporary list which we gonna delete later on couse its immutable

# Tuples and Dictionaries
# the items() method is dictionaries returns a list of (key, value) tuples
# d = dict()
# d["AA"] = 2
# d["BA"] = 4
# for (k,v) in d.items():
#    print(k,v) #AA 2 | BA 4
# tups = d.items()
# print(tups) # dict_items([('AA', 2), ('BA', 4)])

# Tuples are Comparable
# the comparison operators <> work with tuples and other sequences if the first item is equal, python
# goes on to the next element, and so on until it finds elements that differ without checking ones beyond it

# Sorting Lists of Tuples
# we can take advantage of the ability to sort a list of tuples to get a sorted version o a dictionary
# first we sort the dictionary by they key using the items() method and sorted() function
# dict = {"a": 10, "b": 1, "c": 22}
# dict.items() #([('a', 10), ('c', 22), ('b', 1)])
# sorted(dict.items()) #[('a', 10), ('b', 1), ('c', 22)]

# Using sorted()
# We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence
# d = {'a':10, 'b':1, 'c':22}
# t = sorted(d.items())
# print(t) # [('a', 10), ('b', 1), ('c', 22)]
# for k, v in sorted(d.items()):
#    print(k, v) # a 10| b 1 | c 22

# Sort by Values Instead of Key
# we can construct a list of tuples of the form (value, key) so we can  sort by value
# we do this with a for loop that creates a list of tuples
# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k, v in c.items():
#     tmp.append( (v, k) )
# print(tmp) # [#(10, 'a'), (22, 'c'), (1, 'b')]
# tmp = sorted(tmp, reverse=True)
# print(tmp) ##[(22, 'c'), (10, 'a'), (1, 'b')]

# How to print out top 10 most common words
# fhand = open("random_file.txt")
# counts = {}
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0 ) + 1
# lst = []
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# for val, key in lst[:10] :
#     print(key, val)

#                                                                               Regular Expressions
# clever “wild card” expressions for matching and parsing strings

# Understanding Regular Expressions
# very powerful and quite cryptic
# regular expressions are a language unto themselves
# a language of “marker characters” - programming with characters
# it is kind of an “old school” language - compact

# The Regular Expression Module
# before you can use regular expressions in your program, you must import the library using “import re”
# you can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings
# you can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing:  var[5:10]

# Regular Expression Quick Guide
# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

# Using re.search() Like find()
# hand = open('mbox-short.txt')   # hand = open('mbox-short.txt')
# for line in hand:               # for line in hand:
#     line = line.rstrip()        #     line = line.rstrip()
#     if line.find('From:') >= 0: #     if re.search('From:', line) :
#         print(line)             #  print(line)

# Using re.search() Like startswith()
# hand = open('mbox-short.txt')         # hand = open('mbox-short.txt')
# for line in hand:                     # for line in hand:
#     line = line.rstrip()              #     line = line.rstrip(
#     if line.startswith('From:') :     #     if re.search('^From:', line) :
#         print(line)                   # print(line)

# Fine-Tuning Your Match
# depending on how “clean” your data is and the purpose of your application, you may want to narrow your match down a bit
# ^X-\S+:
# ^  match the start of the line
# \S match any non-whitespace character
# + one or more times

# Matching and Extracting data
# re.search() returns a True/False depending on whether the string matches  the regular expression
# if we actually want the matching strings to be extracted, we use re.findall()
# [0-9]+ one or more digits
# import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+',x)
# print(y) # ['2', '19', '42']
# if there is no match we will get empty list
# import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+',x)
# print(y) # ['2', '19', '42']
# y = re.findall('[AEIOU]+',x) AEIOU in any of those in upper case
# >>> print(y) # []

# Warning: Greedy Matching
# the repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string
# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y) #['From: Using the :']
#  ^F first character in the match is an F
# : last character in the match is a :
# .+ one or more characters

# Non-Greedy Matching
# not all regular expression repeat codes are greedy!  You have to add ? to make it not greedy
# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+?:', x)
# print(y) # ['From:']
# ^F first character in the match is an F
# : last character in the match is a :
# .+? one or more characters but not greedy

# Fine-Tuning String Extraction
# you can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# y = re.findall('\S+@\S+',x)
# print(y) #['stephen.marquard@uct.ac.za’]
# \S+@\S+ at least one non-whitespace character with @ in it

# Fine-Tuning String Extraction
# parentheses() are not part of the match - but they tell where to start and stop what string to extract
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# y = re.findall('\S+@\S+',x)
# print(y) # ['stephen.marquard@uct.ac.za']
# y = re.findall('^From (\S+@\S+)',x)
# print(y)  # ['stephen.marquard@uct.ac.za']

# String Parsing examples
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# atpos = data.find('@')
# print(atpos) # 21
# sppos = data.find(' ',atpos)
# print(sppos) # 31
# host = data[atpos+1 : sppos]
# print(host) # uct.ac.za

# The Double Split Pattern
# sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# words = line.split()
# email = words[1] #stephen.marquard@uct.ac.za
# pieces = email.split('@') ['stephen.marquard', 'uct.ac.za']
# print(pieces[1]) # 'uct.ac.za'

# The Regex Version
# import re
# lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('@([^ ]*)',lin)
# print(y) # ['uct.ac.za']
# '@([^ ]*)'
# @ - look through the string until you find an at sign
# [^ ] - match non-blank character
# * - match many of them
# (  ) extract the non-blank characters

# Even Cooler Regex Version
# import re
# lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('^From .*@([^ ]*)',lin)
# print(y) # ['uct.ac.za']
# '^From .*@([^ ]*)'
# ^ - starting at the beginning of the line
# From - look for the string 'From '
# . * - skip a bunch of characters,
# @ - looking for an at sign
# ( - start extracting
# [^ ] - match non-blank character
# + - match many of them
# ) - stop extracting

# Escape Character
# if you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'
# import re
# x = 'We just received $10.00 for cookies.'
# y = re.findall('\$[0-9.]+',x)
# print(y) # ['$10.00']
# \$[0-9.]+
# \$ - look for a real dollar sign
# [0-9.] - a digit or period
# + - at least one or more

#                                                           Networked Programs
# TCP Connections / Sockets
# In computer networking, an Internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across
# an Internet Protocol-based computer network, such as the Internet
# process ( browser xyz) <-- internet --> process ( random web site)

# TCP Port Numbers
# a port is an application-specific or process-specific software communications endpoint
# it allows multiple networked applications to coexist on the same server
# there is a list of well-known TCP port numbers (wikipedia)

# Most Common TCP Ports
# Telnet(23) - Login                        # IMAP (143/220/993) - Mail
# SSH(22) - Secure Login                    # POP (109/110) - Mail Retrieval
# HTTP(80) - talking to web server          # DNS (53) - Domain Name
# SMTP (25) - (Mail)                        # FTP( 21) - File Transfer

# Sockets in Python
# python has built-in support for TCP Sockets
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect( ('data.pr4e.org', 80) )
# host - data.pr4e.org
# port - 80
# socket.SOCK_STREAM - series of characters which come one after another rather than block of series of text

# Application Protocols
# -  mail
# -  world wide web

# HTTP - Hypertext Transfer Protocol
# the HyperText Transfer Protocol is the set of rules to allow browsers to retrieve web documents from servers over the Internet
# the dominant Application Layer Protocol on the Internet
# invented for the Web - to Retrieve HTML,  Images, Documents, etc.
# extended to retrieve data in addition to documents - RSS, Web Services, etc.  Basic Concept - Make a Connection - Request a document - Retrieve the Document - Close the Connection

# What is a Protocol?
# a set of rules that all parties follow so we can predict each other’s behavior
# and not bump into each other
#  - on two-way roads in USA, drive on the right-hand side of the road
#  - on two-way roads in the UK, drive on the left-hand side of the road
# http://www.dr-chuck.com/page1.htm
# http:// - protocol
# www.dr-chuck.com/page1 - host
# page1.htm - document

# Getting Data From The Server
# each time the user clicks on an anchor tag with an href= value to switch to a new page, the browser makes a connection
# to the web server and issues a “GET” request - to GET the content of the page at the specified URL
# the server returns the HTML document to the browser, which formats and displays the document to the user

# Internet Standards
# the standards for all of the Internet protocols (inner workings) are developed by an organization
# internet Engineering Task Force (IETF)
# www.ietf.org
# standards are called “RFCs” - “Request for Comments
