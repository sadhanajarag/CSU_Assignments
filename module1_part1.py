#Addition and Substraction of two number

# Get 1st number
num1 = float(input("Enter the first number: "))

# Get 2nd number
num2 = float(input("Enter the second number: "))


if __name__== "__main__":
    # add two numbers 
    num_add = num1 + num2
    print (f"Addition of {num1} + {num2} =  {num_add} ")

    # substract second number from first number 
    num_sub_1 = num1 - num2
    print (f"Substraction of {num1} - {num2} =  {num_sub_1} ")

    # substract first number from second number 
    num_sub_2 = num2 - num1
    print (f"Substraction of {num2} - {num1} =  {num_sub_2} ")