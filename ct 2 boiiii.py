import random
myList=[]


def mainProgram():
    while True:
        try:
            print("Hey there! Lets work with lists!")
            print("Choose one of the following options. Type a NUMBER ONLY!")
            choice = input("""
1. Add to list,
2. Add a bunch of numbers,
3. Return the value at an index position,
4. Print contents of list,
6. Linear Search
5. Random Choice
7. End Program   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                print(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            else:
                break
        except:
            print("An error occurred")

def addToList():
    newItem = input("Please type an intager!   ")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("we're going to add a BUNCH of numbers!")
    numToAdd = input("How many integers do you want to add?   ")
    numRange = input("And how high would you like these numbers to go to?   ")
    for x in range(0,int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete!")

def indexValues():
    indexPos = input("At what index position would you like to look?   ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value form your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list in the WORST WAY POSSIBLE! cause i want you to suffer")
    searchItem = input("What are you looking for? Number-wise?   ")
    for x in range(len(myList)):
       if myList[x] == int(searchItem):
           print("Your item is at index {}".format(x))

if __name__ == "__main__":
    mainProgram()
