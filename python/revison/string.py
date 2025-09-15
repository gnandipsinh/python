#Q.1



greet= "how are you"

farewell = 'cooming soon'


multiline= '''this is 
multiline'''


print(greet)

print(farewell)

print(multiline)


#Q.2



word  = "sarvaiya"


print(word[0])

print(word[2])

print(word[-1])

print(word[-4])


#Q.3




word = "parthraj123456"

print(word.isalpha())

print(word.isdigit())


print(word.isalnum())


#Q.4
word = "welcome  to sarvaiya parthrajsinh"



print(word[0:7])

print(word[0:18])

print(word[:18])

print(word[0:])

print(word[:-1])

#Q.5




fruits = "apple,banana,mango"



print(fruits.split("a"))


#Q.6


word1="how are you"


word2="good afternoon"


greet = "-".join([word1,word2])

print(greet)


#Q.7

word ="parthrajsinh sarvaiya"

print(word.upper())

print(word.lower())

print(word.title())

print(word.capitalize())




#Q.8




word = "       sarvaiya          "

print(len(word))


word1=word.strip()

word2= word.lstrip()

word3 = word.rstrip()

print(len(word1))



#Q.9





word = "hello good Morning"


print(word.find("mood"))

print(word.find("z"))


print(word.startswith("m"))


print(word.endswith("g"))

print(word.replace("hello","hi"))



#Q.10




bike = "tvs"


year = 2025


print(f"i have {bike} and this is {year} model")