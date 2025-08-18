# Category	       Data Types
# Basic Types	   int, float, str, bool, None
# Sequence Types   list, tuple, range
# Set Types	        set, frozenset
# Mapping Type	    dict
# Binary Types	    bytes, bytearray, memoryview





# 🧠 1. Primitive (Basic) Data Types
# 🔢 int (Integer)
# Whole numbers without a decimal point.

# Can be positive or negative.

x = 10
y = -7
print(type(x))  # <class 'int'>



# 🔣 float (Floating-point)
# Numbers with decimals or in exponential form.

pi = 3.14159
exp = 2e2  # 2 * 10^2 = 200.0
print(type(pi))  # <class 'float'>


# 🔡 str (String)
# Text data enclosed in ' or ".

# Strings can be multi-line using ''' ''' or """ """.


name = "Alice"
message = 'Hello, world!'
multiline = """This is
a multiline string."""
print(type(name))  # <class 'str'>


# ✅ bool (Boolean)
# Represents True or False values (used in logic and conditions).


is_active = True
is_admin = False
print(type(is_active))  # <class 'bool'>


# 📚 2. Sequence Types
# 📋 list
# Ordered, changeable (mutable) collection.

# Can hold items of mixed data types.

fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"
print(fruits)  # ['orange', 'banana', 'cherry']



# 🔗 tuple
# Ordered, unchangeable (immutable) collection.

# Often used when you want to protect data from changes.

dimensions = (1920, 1080)
# dimensions[0] = 1280  # This will cause an error
# print(type(dimensions))  # <class 'tuple'>

# 🔁 range
# Represents a sequence of numbers, often used in loops.

r = range(5)
print(list(r))  # [0, 1, 2, 3, 4]


# 🧩 3. Set Types
# 🎯 set
# Unordered, unchangeable (but mutable), no duplicate items.

# Good for checking membership or eliminating duplicates.


colors = {"red", "green", "blue", "green"}
print(colors)  # {'red', 'green', 'blue'} - no duplicates


# 🧊 frozenset
# Like set, but immutable (cannot be changed after creation).


fs = frozenset([1, 2, 3])
# fs.add(4)  # This will cause an error
print(fs)


# 🧭 4. Mapping Type
# 🗺️ dict (Dictionary)
# A collection of key-value pairs.

# Keys must be unique and immutable (usually strings or numbers).

# Values can be any type.

person = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}
print(person["name"])  # Alice


# 🚫 5. None Type
# 🕳️ None
# Special value used to represent “nothing” or “no value”.

# Often used as a placeholder or return value when there’s no result.


x = None
print(type(x))  # <class 'NoneType'>

# 🔌 6. Binary Types
# 🧱 bytes
# Immutable sequence of bytes (0–255).

# Common in file handling, networking, images, etc.



b = b"hello"
print(type(b))  # <class 'bytes'>

# 🧱 bytearray
# Like bytes but mutable.


ba = bytearray([65, 66, 67])
ba[0] = 68  # Changing value
print(ba)  # bytearray(b'DBC')

# 🧠 memoryview
# Used to access internal data of an object without copying.

# Mostly used for large binary data handling.


mv = memoryview(b"abc")
print(mv[0])  # 97 (ASCII of 'a')