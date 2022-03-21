# Christmas Tree
def crown(n):
    for i in range(n):
        for x in range(n-i):
            print(' ', end=' ')
        for y in range(2*i+1):
            print('*', end=' ')
        print()

def trunk(n):
    for x in range(3):
        for i in range(n-1):
            print(' ', end=' ')
        print('* * *')

def christmastree():
    row = int(input('Enter number of rows: '))
    crown(row)
    crown(row)
    trunk(row)


# Ship
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"


def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    |\   ")
    print(sp + "    |/   ")
    print(SHIP_COLOR, end="")
    print(sp + "\__ |__/ ")
    print(sp + " \____/  ")
    print(RESET_COLOR)

def ship():
  
    start = 0
    distance = 60
    step = 2
    for position in range(start, distance, step): 
      ship_print(position)

# Swap
def swap():
    a = int(input("First Number?: "))
    b = int(input("Second Number?: "))
    if a > b:
        print(b,a)
    else:
        print(a,b)

def f1():
    print('f1')
def f2():
    print('f2')

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")
    print("What is your choice? (enter the number value) ")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input())
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()
        else:
            presentMenu(menu[choice]["exec"])

def print_matrix():
    matrix = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    for x in matrix:
        print(*x)

subMenu = {
    1: {"display":"f1",
        "exec":f1,
        "type":"func"},
    2: {"display":"f2",
        "type":"func",
        "exec":f2,}
}

mainMenu = {
    1: {"display":"Christmas Tree",
        "exec":christmastree,
        "type":"func"},
    2: {"display":"Ship",
        "exec":ship,
        "type":"func"},
    3: {"display":"Keypad ",
        "exec":print_matrix,
        "type":"func"},
    4: {"display":"Swap ",
        "exec":swap,
        "type":"func"},
    5: {
        "display":"Submenu",
        "exec": subMenu,
        "type":"submenu"
    }
}

if __name__ == "__main__":
    presentMenu(mainMenu)





