#Multiplication  and Division of two number

# Get 1st number
num1 = float(input("Enter the first number: "))

# Get 2nd number
num2 = float(input("Enter the second number: "))


if __name__== "__main__":
    # Multiply two numbers 
    num_mul = num1 * num2
    print (f"Multiplication of {num1} * {num2} =  {num_mul} ")

    # Divide num1/num2
    if num2 == 0:
        print("In devision second number should not be zero")
    else:

        num_div = num1 / num2
        print (f"Division of {num1} / {num2} =  {num_div} ")

