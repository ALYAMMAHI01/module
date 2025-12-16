# function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def print_variable_info(var):
    print(var)
    return f"{var} {type(var)}"

# Example usage
if __name__ == "__main__":
    # Test the print_variable_info function
    result = print_variable_info(42)
    print("Returned:", result)
    
    result = print_variable_info("Hello")
    print("Returned:", result)

