print("Welcome to the Amazing Digital Animal Fact Giver v.0.01!")
import random
version = 0.02
print("Disclaimer: Insects are not included (i'm entomophobic)")
print("Below is a list of all animals in the system as of [JULY 6, 2026]: ")
print("cat, dog, rabbit, turtle, gecko, sheep (try variations like puppy, kitty, bunbun or sea turtle too!)")
print("Type 'HELP' instead of Y/N below for a full updated list of variations and allowed syntax for the search query!")
ans = input("Would you like to ask for an animal fact? (Y/N): ")

while ans == "HELP" or ans == "help":
    print("Below is an updated list of variations and syntax to help you search!")
    print("More liberties will be added as version grows. CURRENT VERSION:", version)
    print("would you like to see ALLOWED SYNTAX or VARIATIONS? (spell these correctly por favor)")
    shamura = input()
    if shamura == "ALLOWED SYNTAX" or shamura == "Allowed Syntax" or shamura == "allowed syntax" or shamura == "syntax" or shamura == "SYNTAX" or shamura == "Syntax":
        print("Okay! Below is a list of ALLOWED SYNTAX as of version", version)
        print("All lowercase (case sensitive), no spaces, plural allowed")
        shamura = input("Would you like to see VARIATIONS or would you like to SEARCH already? ")
    if shamura == "SEARCH ALREADY" or shamura == "search already" or shamura == "Search Already" or shamura == "search" or shamura == "Search" or shamura == "SEARCH":
            ans = "Y"
    if shamura == "VARIATIONS" or shamura == "Variations" or shamura == "variations":
        print("Below is the full list of allowed variations for the following animals as of version", version)
        print("CAT: cat, cats, kitty, kitties, kitten, kittens, kittycat, kittycats, pussycat, pussycats")
        print("DOG: dog, dogs, puppy, puppies, puppydog, pup, pups, puppydogs")
        print("RABBIT: rabbit, rabbits, bunny, bunnies, bun, buns, bunbun, bunbuns")
        print("TURTLE: turtle, turtles, sea turtle, sea turtles")
        print("GECKO: gecko, geckos, gecky, geckies")
        print("SHEEP: sheep, sheeps, lamb, lambs")
        shamura = input("Would you like to see the ALLOWED SYNTAX or SEARCH already? ")

while ans == "Y" or ans == "y":
    animal = input("What animal would you like to learn about today?: ")
    #COLLAPSE THIS LMAOOOOOO
    if animal == "cat" or animal == "kitty" or animal == "kittycat" or animal == "kittycats" or animal == "pussycat" or animal == "pussycats" or animal == "cats" or animal == "kitties" or animal == "kitten" or animal == "kittens":
        print("Not many people know that cats have an organ in the roof of their mouth called the vomeronasal organ (or Jacobson's organ).")
        print("This organ allows cats to inspect scents and pheromones more throroughly.")
        print("When cats use it, they make a rather funny face called the flehmen response (look up pictures on this online, it's funny)")
        ans = input("Would you like to ask about another animal? (Y/N): ")
    elif animal == "dog" or animal == "puppy" or animal == "puppydog" or animal == "pup" or animal == "dogs" or animal == "puppies" or animal == "puppydogs" or animal == "pups":
        print("Laika the Dog was the first dog to go to space in 1952!")
        print("She was a stray Russian mutt.")
        print("Unfortunately, she died of intense heat while reentering the atmosphere.")
        print("Luckily, nowadays that.. doesn't happen!")
        print("Oh also dog urine can corrode and break down metal")
        print("... that's cool right")
        ans = input("Would you like to ask about another animal? (Y/N): ")
    elif animal == "rabbit" or animal == "bunny" or animal == "rabbits" or animal == "bunnies" or animal == "bunbun" or animal == "bunbuns" or animal == "bun" or animal == "bunbuns":
        print("Did you know that rabbits cannot regurgitate? That's cool!")
        print("Also, average pet store rabbit cages are not big enough for rabbits (on average they are 7 lbs)")
        print("and and and also also also umm umm ummmmm")
        print("they have 360 vision and there are many different breeds of rabbit and and um um um")
        print("they are very social and are NOT rodents")
        print("and also stubbron sometimes")
        print("Also they are the most abandoned type of pet!!! #justiceforbunbuns")
        ans = input("Would you like facts about another animal? (Y/N): ")
    elif animal == "turtle" or animal == "turtles" or animal == "sea turtles" or animal == "sea turtle":
        print("Sea turtles are an endangered species!")
        print("Turtles don't have teeth!")
        print("A sea turtle can live for over 100 years.")
        print("Only 1 in 1000 sea turtles survive to adulthood.")
        ans = input("Would you like to search for another animal?")
    elif animal == "gecko" or animal == "geckos" or animal == "gecky" or animal == "geckies":
        print("Geckos are mostly nocturnal lizards.")
        print("Geckos have a really strong sense of smell.")
        print("Geckos are NOT low-maintenance!!!")
        ans = input("Would you like facts about another animal?")
    elif animal == "sheep" or animal == "sheeps" or animal == "lamb" or animal == "lambs":
        print("Sheep have incredible facial recognition.")
        print("They can recognize and remember up to 50 sheep faces and at least 10 human faces for over two years!")
        print("They can also see between 270 and 320 degrees without moving their heads!")
        print("To put things into perspective, we can only see 120 to 130 degrees without moving our heads.")
        ans = input("Would you like facts about another animal?")


if ans == "N" or ans == "n":
    print("Okay, goodbye! Start me again if you ever change your mind. :3")

