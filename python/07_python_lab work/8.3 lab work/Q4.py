





update_id = int(input("Enter student ID to update marks: "))
new_marks = int(input("Enter new marks: "))

for s in students:
    if s["id"] == update_id:
        s["marks"] = new_marks
        print("Marks updated.")
        break
else:
    print("Student not found.")

print("Updated list:", students)
