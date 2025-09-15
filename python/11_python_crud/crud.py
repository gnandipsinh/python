
students=[]

while True:
    print("\n--- Student Management ---")
    print("1. Show students")
    print("2. Add student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

    choice=input("enter your choice ")


 # Read

    if choice == "1":
        if students == []:
            print("no student data found")
        else:
            for s in students:
                print("ID",s["id"],"Name",s["name"])

# create
    elif choice == "2":
        name=input("enter your name")
        sId=len(students)+1

        students.append({"id":sId,"name":name})
        print("student added")
# update
    elif choice == "3":

        sId= int(input("enter id to update: "))
        for s in students:
            if s["id"] == sId:
                s["name"] = input("enter new name")
                print("student data updated")
                break
        else:
            print("student with this id not found")


# Delete

    elif choice == "4":
        sId=int(input("enter id to delet"))
        for s in students :
            if s["id"] == sId:
                students,remove(s)
                print("sudent data deleted")
                break
    
            else:
                 print("no student data ")

    elif choice == "5":
        print("good by")
        break

    else:
        print("invalid choise please choos correctly")
