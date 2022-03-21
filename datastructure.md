{% include navigation.html %}
# Data Structures


## Week 1
Python Lists Vs Dictionaries

List is a collection of index values pairs as that of array in JS. Dictionary is a hashed structure of key and value pairs.
InfoDB Lists
KVDb = []
#### List with dictionary records placed in a list  
```
ASDb.append({  
               "FirstName": "Armaan",  
               "LastName": "Shamsaasef",  
               "Date Of Birth": "November 17, 2004",  
               "Location": "San Diego",  
               "Personal Email": "armaan.shamsaasef@gmail.com",    
              })  
 ```
              
Print the second car from Mortensen’s Owns_Cars list
```
x = InfoDb[0]["Coding_Languages"][1] 
result: John Mortensen
```
There is also a method called get() on the Dictionary(InfoDb[0]) that will give you the same result:
```
x = InfoDb[0].get("Coding_Languages")[2]
result: CSS
```

Print Content from InfoDB
#### given an index this will print InfoDb content
```
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
 ```

While Loop
#### while loop contains an initial n and an index incrementing statement (n += 1)
```
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
```
 
For Loop
#### for loop iterates on length of InfoDb
```
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
```
        
## Tri 3 TT0 Python Menu, Replit, Github
Python Menu w/ data structures and try/except statements
```
# menu.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import loopy
import mathpy
import funcy
import patterns


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Stringy", "stringy.py"],
    ["Listy", "listy.py"],
    ["Loopy", loopy.main],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", mathpy.factors],
    ["GCD", mathpy.gcd],
    ["LCM", mathpy.lcm],
    ["Primes", mathpy.primes],
]

patterns_sub_menu = [
    ["Patterns", "patterns.py"],
    ["PreFuncy", "prefuncy.py"],
    ["Funcy", funcy.ship],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
 ```



## Week 0

Final Idea: Site that gives Coding questions, with rewards and surprises for each correct answer (Level System).

Our project is dedicated to the learning, improvement, and utmost enjoyment of coding! We aspire to help beginners improve their coding ability by implementing a series of levels that increase difficulty as they complete the tasks. By the end, they should see themselves as better programmers than before while also having enjoyed the journey. We are Team Siuuuu and are sponsored by Hackclub, a group of coders hoping to teach beginner coders.

[Replit](https://replit.com/@RitvikKeerthi/Data-Structures-Project#index.html)

[Individual Replit](https://replit.com/@ArmaanShamsaase/Armaan-Shamsaasef-2-1#Menu.py)

[Level 1 Code](https://github.com/KoolKidKai/Siuuuu/blob/main/templates/level1.html)

Code Snippets for Key Learnings:

![image](https://user-images.githubusercontent.com/89219486/158040786-9e95a90f-a878-4e34-9806-548a7339d423.png)



How Questions are Created (hoping to shift to a const of questions in the future):)

Response to User Input: ![image](https://user-images.githubusercontent.com/89219486/158040797-19121083-7785-41ee-ab58-bde0cc441e94.png)

Key Features that are in Progress: Scoring system to reward players if answer is correct Key Features that are in Progress: Link to replit for harder levels if code is > 1 line (so that we don't run into errors with the .value call)
![image](https://user-images.githubusercontent.com/89219486/158040920-5345f10d-bf95-482f-b319-c32c468c5956.png)
![image](https://user-images.githubusercontent.com/89219486/158040923-c5733999-8dd3-4a59-ad57-8c06a9514bc5.png)
