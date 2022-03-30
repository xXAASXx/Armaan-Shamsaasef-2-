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


if __name__ == "__main__":
    christmastree()