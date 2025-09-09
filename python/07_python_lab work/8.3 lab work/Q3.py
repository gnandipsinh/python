







search_id = int(input("Enter student ID to search: "))
for s in students:
    if s["id"] == search_id:
        print("Student found:", s)
        break
else:
    print("Student not found.")
