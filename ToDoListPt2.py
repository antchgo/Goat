#Holy Moly
#Scarlett Arroyo and Tony Garcia
#1/11/24
#To-Do List

#Initialize        
myList = []
symbolList = ["✓", "☒", "☺"]
#Functions
def toDolist():
    while True:
        global myList
        print("1. Add task to list \n2. View list \n3. Complete a task \n4. Remove a task \n5. Exit \n6.remove all task \n7. Sort the list alphabetically \n8. Print the number of items on list")
        option=int(input("Option:"))
        if option == 1:
            newtask = input("What would you like to add:")
            myList.insert(0, newtask)
            print (myList)
        if option == 2:
            print(myList)
        if option == 3:        
            print(myList)
            done = input("what task is completed")
            a = myList.index(done)
            myList.insert(a,"X")
            myList.remove(done)
            print(myList)
        if option == 4:
            print(myList)
            remove = input("What task do you want to remove?")
            i = myList.index(remove)
            myList.remove(remove)
            print(myList)
        if option == 5:
            print("goodbye")
            break
        if option == 6:
            myList.clear()
            print(myList)
        if option == 7:
            myList.sort()
            print(myList)
        if option == 8:
            print(len(myList))
            

#Main
toDolist()