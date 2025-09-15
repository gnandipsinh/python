

# def functionName (parameter):
#     return

# optional: parameter and return value in function




# example 

def greet():
    print("hello")


greet()    


# with parameter 


def add(a,b):
    print(a+b)
    print(a*b)


add(5,10)


# with return value

def square(num):
    return num+num


result = square(6)

print(result)


# with default parameter


def createAccount(name,amount=2000):
    print("account created of ",name, "and total balance ",amount)



createAccount("john")


createAccount("alice",5000)
