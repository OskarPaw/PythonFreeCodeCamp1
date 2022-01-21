# list = used to store multiple items in a single variable, I can make changes in it by
# food.commands

food = ["Pizza","Hamburger","Hotdog","Spaghetti","Pudding"]

food[0] = "Sushi"

print(food[0])

food.append("Ice cream")
food.remove("Hotdog")
food.pop() #usuwa ostnią pozycję wpisaną
food.insert(0,"Cake") #podmienia daną pozcyję na wybrany wyraz
food.sort() #sortuję listę alfabetycznie
#food.clear() usuwa całą listę

for x in food:
    print(x)

#2D lists(multi-dimensional lists) = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["Pizza","Hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]

print(food)
print(food[0][0])
print(food[1][0])
print(food[1][2])
print(food[1][1])

# tuple = niezmienny typ danych,że można z niej pobierać dane ale nie można ich modyfikować
# ani usuwać.Powinna być zatem używana wszędzie tam, gdzie dane muszą być stałe. charakteryzują
#ją ()

student = ("Oskar",20,"male")

print(student.count("Oskar"))
print(student.index("male"))

for x in student:
    print(x)

if "Oskar" in student:
    print("Oskar is here!")

# set/zbiór = collection which is unordered,unindexed.No duplicates values

utensils = {"fork","spoon","knife","knife","knife"}
dishes =  {"bowl","plate","cup"}

utensils.add("napkin") #dodaje wybrany element
utensils.remove("fork") #usuwa wybrany  fragmenty
#utensils.clear() #usuwa całość
#utensils.update(dishes) # wprowadza zbiór w inny zbiór
dinner_table = utensils.union(dishes) #całkowicie nowy set który zawiera wcześniejsze wybrane przez nas sety

for x in utensils:
    print(x)
for x in dinner_table:
    print(x)

tes1 = {"łyżka","knife","fork"}
tes2 = {"tależ","knife"}

print(tes1.difference(tes2)) #różne rzeczy w liście
print(tes1.intersection(tes2)) # wspólne rzeczy w liście
