
try:
    num1 = float(input("Enter first Number: ")) # input first number (used float to work with decimal numbers also)
    num2 = float(input("Enter Second Number: ")) # input second number (used float to work with decimal numbers also)

    print("Addition of ", num1 ,"and", num2, "is: ", num1+num2 )  # Addition
    print("Substraction of ", num1 ,"and", num2, "is: ", num1-num2 )    # Substraction
    print("Multiplication of ", num1 ,"and", num2, "is: ", num1*num2 )    #  Multiplication
    print("Division of ", num1 ,"and", num2, "is: ", num1/num2 )  #  Division
    #Write your code here

    exam1= float(input("Enter marks for Exam1: "))   # input marks for exam 1
    exam2= float(input("Enter marks for Exam2: "))   # input marks for exam 2
    exam3= float(input("Enter marks for Exam3: "))   # input marks for exam 3

    print("Final Grade is: ", (exam1+exam2+exam3)/3)     #   printing output value

except ZeroDivisionError:          #  Handling divide by zero error
    print("Cannot divide a number by 0")
    
except ValueError:     # Handling Value error
    print("Enter integer or float number only")

except NameError:     # Handling Name error
    print("Variable does not exist")
    
except:            # other exceptions
    print("Some other Exception, Hope I handled all exceptions in above statements")
















