from Week0.tree import christmastree
from Week0.ship import ship
from Week0.matrix import print_matrix
from Week0.swap import swap

from Week1.fib import fibonacci
from Week1.listloops import loops

from Week2.factorialCALL import printfac
from Week2.MATH import trian
from Week2.Palindrome import pal
  

week0 = {
    1: {
        "display":"Christmas Tree",
        "exec":christmastree,
        "type":"func"
    },
    2: {
        "display":"Ship",
        "exec":ship,
        "type":"func"},
    3: {
        "display":"Keypad ",
        "exec":print_matrix,
        "type":"func"},
    4: {
        "display":"Swap ",
        "exec":swap,
        "type":"func"},
    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}
week1 = {
  1: {
    "display": "Fibonacci",
    "exec": fibonacci,
    "type": "func"
  },
  2: {
    "display": "Lists & Loops",
    "exec": loops,
    "type": "func"
  },
  0: {
    "display": "Quit",
    "exec": quit,
    "type": "func"
  }
}
week2 = {
    1: {
        "display":"Factorial",
        "exec":printfac,
        "type":"func"
    },
    2: {
        "display":"Math Function: Triangular Numbers",
        "exec":trian,
        "type":"func"
    },
    3: {
        "display":"EC: Palindrome",
        "exec":pal,
        "type":"func"
    },
    0: {
        "display":"Quit",
        "exec":quit,
        "type":"func"
    }
}

mainMenu = {
    0: {
        "display": "Week 0",
        "exec": week0,
        "type": "submenu"
    },
    1: {
        "display": "Week 1",
        "exec": week1,
        "type": "submenu"
    },
    2: {
        "display": "Week 2",
        "exec": week2,
        "type": "submenu"
    },

    7: {
        "display": "Quit",
        "exec": quit,
        "type":"func"
    }
}


def buildMenu(menu):
    for key,value in menu.items(): 
        display = value["display"]
        print(f"{key} ------ {display}") # each menu item is printed
    print("What is your choice? (enter the number value) ") # user input promp

def presentMenu(menu):
    buildMenu(menu) #print out menu and take input
    choice = int(input())
    while choice not in menu: # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func": #determine whether recursion is needed
            menu[choice]["exec"]() #run function

        else:
            presentMenu(menu[choice]["exec"]) #display submenu

if __name__ == "__main__":
  while True:
    presentMenu(mainMenu)