






remove_id = int(input("Enter student ID to remove: "))

students = [s for s in students if s["id"] != remove_id]
print("Updated list:", students)
