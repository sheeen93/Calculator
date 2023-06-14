print("Hello! I am Gunsheen Kour and this is my calculator")
print("For multiplication enter '*' ")
print("For addition enter '+' ")
print("For subtraction enter '-' ")
print("For division enter '/' ")

n=input()


def add ():
    p=int(input("Enter the number of integers you want to add"))
    l=[]
    total=0
    for i in range (p):
        r=int(input())
        l.append(r)   
    for j in range(len(l)):
        total= total+l[j]
    print("Your enterd the following integers :- ",l)
    print("The sum is",total)


        
def mul ():
    p=int(input("Enter the number of integers you want to Multiply"))
    l=[]
    total=0
    for i in range (p):
        r=int(input())
        l.append(r)
    for j in range(len(l)):
        total= total*l[j]
    print("Your enterd the following integers :- ",l)
    print("The mulpiply is",total)



def div ():
    x=int(input("Enter the divisor"))
    y=int(input("Enter the divident"))
    
    total = x/y
    print("The remainder is",total)



def sub ():
    p=int(input("Enter the number of integers you want to subtract"))
    l=[]
    total=0
    for i in range (p):
        r=int(input())
        l.append(r)
    for j in range(len(l)):
        total= total-l[j]
    print("Your enterd the following integers :- ",l)
    print("The mulpiply is",total)
        
    
if n=="+":
        add()
elif n=="-":
        sub()

elif n=="*":
        mul()       
        
elif n=="/":
        div()
else:
    print("UNKNOWN COMMAND")
