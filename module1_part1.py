#Progarm for Addition  and Substraction of two numbers

#Import Custom exception class to handle expetion

from Error_handle import CalculatorError 

class AddAndSub:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    # Handle the addtion of two numbers
    def add(self):
        return self.num1 + self.num2
    
     # Handle Substraction of num1 - num2 numbers
    def sub(self):
        sub_result1 = self.num1 - self.num2  
        sub_result2 = self.num2 - self.num1
        return sub_result1,sub_result2
    
 # Main fuction   
def main():
        #define while loop to get choices from user
        while True:
            print("Choose an option:")
            print("1. Addition")
            print("2. Substraction")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice in ['1', '2']:
                  try:
                    #Take input from user
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    # Create an instance of AddAndSub
                    calc = AddAndSub(num1, num2)
                    if choice =='1':
                          # Perform Addition
                          add_result = calc.add()
                          print(f"Addition of {num1} and {num2} is: {add_result}") 
                    elif choice == '2':
                          # Perform Substraction
                          res1,res2= calc.sub()
                          print(f"Subtraction of {num1} and {num2} is: {res1}")
                          print(f"Subtraction of {num2} and {num1} is: {res2}")
                
                #Exception handling block
                  except ValueError as e:
                          print(f"Invalid input: {e}")
                  except CalculatorError as e:
                          print(f"Calculator error: {e}")   
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