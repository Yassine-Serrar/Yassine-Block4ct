import random
myList=[]


def mainProgram():
    while True:
        print("Hey there! Lets work with lists!")
        print("Choose one of the following options. Type a NUMBER ONLY!")
        choice = input("""1. Add to list,
    2. Return the value at an index position,
    3. End Program   """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            break


    def addToList():
        newItem = input("Please type an intager!   ")
        myList.append(int(newItem))
        print(myList)

    def indexValues():
        indexPos = input("At what index position would you like to look?   ")
        print(myList[int(indexPos)])

    def randomSearch():
        print("Here's a random value form your list!")
        print(myList[random.randint(0, len(myList)-1)]

    if __name__ == "__main__":
        mainProgram()
