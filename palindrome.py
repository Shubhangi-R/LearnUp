def is_palindrome(s):
    return s == s[::-1]

 # write code for addition of two number
def add_numbers(a, b):
    return a + b

def sub_numbers(a, b):
    return a - b

def main():
    # Test the function
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
        
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = add_numbers(num1, num2)
    result = sub_numbers(num1, num2)
    
    print("The sum of", num1, "and", num2, "is:", result)
    print("The sub of", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    main()

