
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []

InfoDb.append({
    "FirstName": "LeBron",
    "LastName": "James",
    "Team": "LA Lakers",
    "MVPs": "4",
    "Rings": "4",
    "Teams":["Cleveland Cavs","Miami Heat","LA Lakers"]
})

InfoDb.append({
    "FirstName": "Kevin",
    "LastName": "Durant",
    "Team": "Brooklyn Nets",
    "MVPs": "1",
    "Rings": "2",
    "Teams":["OKC Thunder","Golden State Warriors","Brooklyn Nets"]
})

InfoDb.append({
    "FirstName": "Stephen",
    "LastName": "Curry",
    "Team": "Golden State Warriors",
    "MVPs": "2",
    "Rings": "3",
    "Teams":["Golden State Warriors"]
})


def print_data(i):
    print(InfoDb[i]["FirstName"], InfoDb[i]["LastName"])  
    print("\t", "Teams: ", end="")  
    print(", ".join(InfoDb[i]["Teams"]))  
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def for_loop():
    for i in range(len(InfoDb)):
        print_data(i)

def while_loop(i):
    while i < len(InfoDb):
        print_data(i)
        i += 1
    return


def recursive_loop(i):
    if i < len(InfoDb):
        print_data(i)
        recursive_loop(i+1)
        return



print("For loop")
for_loop()
print("While loop")
while_loop(0)  
print("Recursive loop")
recursive_loop(0)