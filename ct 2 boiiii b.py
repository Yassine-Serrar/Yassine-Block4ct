import random
myList = []
unique_list = []


def mainProgram():
    while True:
        try:
            print("Hey there! Lets work with lists!")
            print("Choose one of the following options. Type a NUMBER ONLY!")
            choice = input("""
1. Add to list,
2. Add a bunch of numbers,
3. Return the value at an index position,
4. Sort list,
5. Random Choice,
6. Linear Search,
7. Recursive Search
8. Print Lists,
9. Find Sum of Numbers,
10. End Program   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                binSearch = input("what number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                printLists()
            elif choice == "9":
                numberSum()
                

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


def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see you new list? Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)


def numberSum():
    lst = []
    num = int(input('would you like to add up?   '))
    for x in range(num):
        numbers = int(input('Number   '))
        lst.append(numbers)
        print("The sum of your numbers are   ",sum(lst))
    
    

def indexValues():
    indexPos = input("At what index position would you like to look?   ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value form your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("""We're going to search through the list in the WORST WAY POSSIBLE!
because i want you to suffer """)
    searchItem = input("What are you looking for? Number-wise?   ")
    for x in range(len(myList)):
       if myList[x] == int(searchItem):
           print("Your item is at index {}".format(x))
    print(indexCount)
    
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Oh, your just a lucky dude aren't you? Your number is at position {}".format(mid))
            return mid

        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)

        else:
            return recursiveBinarySearch(unique_list, low, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whitchOne = input ("Which list? Sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)

if __name__ == "__main__":
    mainProgram()
