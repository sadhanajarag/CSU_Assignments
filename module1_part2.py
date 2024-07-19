#Progarm for Multiplication  and Division of two numbers

#Import Custom exception class to handle expetion

from Error_handle import CalculatorError 

class MulAndDiv:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    # Handle the addtion of two numbers
    def mul(self):
        return self.num1 * self.num2
    
     # Handle Substraction of num1 - num2 numbers
    def div(self):
        return self.num1 /self.num2
    
 # Main fuction   
def main():
        while True:
            print("Choose an option:")
            print("1. Multiplication")
            print("2. Division")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice in ['1', '2']:
                  try:
                    #Take input from user
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    # Create an instance of MulAndDiv
                    calc = MulAndDiv(num1, num2)
                    if choice =='1':
                          # Perform multiplication
                          mul_result = calc.mul()
                          print(f"Multiplication of {num1} and {num2} is: {mul_result}") 
                    elif choice == '2':
                          # Perform division
                          division_result = calc.div()
                          print(f"Subtraction of {num1} and {num2} is: {division_result}")
                  except ValueError as e:
                          print(f"Invalid input: {e}")
                  except CalculatorError as e:
                          print(f"Calculator error: {e}")
                  except ZeroDivisionError as e:
                          print(f"Error: Cannot divide by zero: {e}")        
                  except Exception as e:
                          print(f"An unexpected error occurred: {e}")
                  finally:
                          print("Operation completed.")
            elif choice == '3':
                print("Exiting...")
                break
            else:
              print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()