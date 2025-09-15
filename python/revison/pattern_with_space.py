#Q.1


p=5


[1,2,3,4,5]



for d in range(1,p+1):
    
    for space in range(p - d,0,-1):
    
        print(" ",end=" ")
    for j in range(d,0,-1):
          print(j,end=" ")
    print()



#Q.2




p=5


for i in range(p,0,-1):
    for space in range(i-1):
        print(" ",end=" ")
    for j in range(i,p+1):
        print(j,end=" ")
    print()  



#Q.3




p=5;


for d in range(p,0,-1):
    for space in range(d-1):
        print(" ",end=" ")
    for j in range(p-d+1):
        print(d, end=" ")
    print()        



#Q.4


p= 6

for row in range(p):                        
    print("  " * row, end="")               

    for col in range(p - row):            
        print((row + col) % 2, end=" ")     
    print()



#Q.5



d=8

for i in range(d,0,-1):

    for space in range(d-i):

        print(" ",end=" ")

    for j in range(i,0,-1):

        print(j,end=" ")

    print()        



#Q.6


s = 6
for i in range(s):                        
    for space in range(i):                
        print(" ", end=" ")               
    for num in range(s, i, -1):            
        print(num, end=" ")
    print()                  
