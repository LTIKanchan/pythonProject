# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime


def print_hi(name):
    #name="kanchan"
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_hello(name):
    #name="Bhagya"
    print(f'Hello, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(name.__contains__("a"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    newname = "Kanchan"
    print_hi(newname)
    print_hello(newname)
    name = "Kanchan"
    flag = True
    x = 0
    y = 1.1
    datenew = datetime.today()
    print(str(type(name))+" "+name)
    print(type(flag))
    print(type(x))
    print(type(y))
    print(type(datenew))
    print("The todays date is "+ str(datenew))
