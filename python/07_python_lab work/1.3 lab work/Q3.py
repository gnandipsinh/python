







bool_val = input("Enter True or False: ")
bool_val = bool_val.lower() == "true"   

int_val = int(bool_val)
str_val = str(bool_val)

print("Boolean:", bool_val, "| Type:", type(bool_val))
print("As Integer:", int_val, "| Type:", type(int_val))
print("As String:", str_val, "| Type:", type(str_val))
