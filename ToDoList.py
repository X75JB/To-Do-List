+# This is a todolist
# Jackson Blackman
# 2022-09-20

# imports
import os


# Opens txt file
def openfile():
    global lines
    file = open('list.txt', 'r')
    lines = file.readlines()
    file.close()


# prints the list
def readtodolist():
    for i in range(len(lines)):
        print(str(i + 1) + " - " + lines[i].strip("\n"))


# removes your choice
def removal():
    choice = int(input("Which item would you like to remove? "))
    lines.remove(lines[choice - 1])


# Adds to the list
def add():
    tobeadded = input('What would you like to add to your todo list? \n')
    lines.append('\n' + tobeadded)


# Closes txt file
def closefile():
    file = open('list.txt', 'w')
    file.writelines(lines)
    file.close()


# Program starts

openfile()

while True:
    os.system('cls')
    readtodolist()
    userchoice = input('What would you like to do with your list? A - add | R - remove | C - close \n:').capitalize()
    if userchoice == 'A':
        add()
    if userchoice == 'R':
        removal()
    if userchoice == 'C':
        break
    elif userchoice:
        print('Invalid choice')

closefile()
