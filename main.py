# Define the animals as strings
Dog = "Dog"
Cats = "Cats"
Parrot = "Parrot"
Snake = "Snake"

pets = {
    "Marley": Dog,
    "Bob": Cats,
    "Charlie": Parrot
}

# add new Student
pets["David"] = Snake
del pets["Charlie"]

print("Initital Animals and Owners:", pets)
 
for name, pets in pets.items():
    print(f"Name: {name}\tpets: {pets}")
    
# Define the People as Strings
SamGill = "Sam Gill"
HarvirBasketballLover = "Harvir Basketball Lover <}"
PreetyPreet = "Preety Preet"

People = {
    "778-6970-482": SamGill,
    "604-618-1137": HarvirBasketballLover,
    "236-5512-983": PreetyPreet
}

print("Initital Animals and Owners:", People)
 
for name, People in People.items():
    print(f"Number: {name}\tPeople: {People}")
    
