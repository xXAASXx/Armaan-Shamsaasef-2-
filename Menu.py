from Week0.tree import christmastree
from Week0.ship import ship
from Week0.matrix import print_matrix
from Week0.swap import swap

from Week1.fib import fibonacci
from Week1.listloops import loops

from Week2.factorialCALL import printfac
from Week2.MATH import trian
from Week2.Palindrome import pal
  

Drawing = {
    1: {
        "display":"Christmas Tree",
        "exec":christmastree,
        "type":"func"
    },
    2: {
        "display":"Ship",
        "exec":ship,
        "type":"func"},
    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}
Info = {
  1: {
    "display": "Lists & Loops",
    "exec": loops,
    "type": "func"
  },
  2: {
    "display":"Keypad ",
    "exec":print_matrix,
    "type":"func"},
  3: {
    "display":"Swap ",
    "exec":swap,
    "type":"func"},
  0: {
    "display": "Quit",
    "exec": quit,
    "type": "func"
  }
}
Math = {
    1: {
        "display":"Factorial",
        "exec":printfac,
        "type":"func"
    },
    2: {
      "display": "Fibonacci",
      "exec": fibonacci,
      "type": "func"
    },
    3: {
        "display":"Math Function: Triangular Numbers",
        "exec":trian,
        "type":"func"
    },
    4: {
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
        "display": "Drawings",
        "exec": Drawing,
        "type": "submenu"
    },
    1: {
        "display": "Info",
        "exec": Info,
        "type": "submenu"
    },
    2: {
        "display": "Mathematics",
        "exec": Math,
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