def add(x,y):
    return x+y

def Subtract(x,y):
    return x-y

def Multiple(x,y):
    return x*y

def Division(x,y):
    if y == 0:
        #print "cant divide by zero"
        return "cant divide by zero"
    else:
        return x/y


print "selection option"
print "Addition - 1 "
print "Subtraction - 2 "
print "Multiplication - 3 "
print "Division - 4 "

while True :
    choice = input("select 1 or 2 or 3 or 4 for your calculations :")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter your 1st number"))
        num2 = float(input("Enter your 2nd number"))

        if choice == '1':
            print ("Result : ",add(num1,num2))
        elif choice == '2':
            print ("Result : ",Subtract(num1,num2))
        elif choice == '3':
            print ("Result : ",Multiple(num1,num2))
        elif choice == '4' :
            print ("Result : ",Division(num1,num2))

        break
    else:
        print "Invalid input"







