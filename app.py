from cal_fun import do_addition, do_subtraction
from multiply import do_multiplication

def main():
    print('Welcome to the Calculator app')
    print("""
Select the function from the given options:
1. Add
2. Subtract
3. multiply
    """)

    try:
        user_input = input("Select the function: ")
        print(f"User selected option: {user_input}")
        
        a = int(input("Value of A: "))
        print(f"Value of A: {a}")
        b = int(input("Value of B: "))
        print(f"Value of B: {b}")
      
        if user_input == "1":
            result = do_addition(a, b)
        elif user_input == "2":
            result = do_subtraction(a, b)
        elif user_input == "3":    
            result = do_multiplication(a,b)
        else:
            print("Invalid selection")
            return

        print('Result:', result)
    except Exception as e:
        print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()
