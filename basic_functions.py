

def add(num1, num2):
     adding = num1 + num2  # Implement addition
     return adding

def subtract(num1, num2):
    minus = num1 - num2  # Implement subtraction
    return minus

def multiply(num1, num2):
    product = num1 * num2  # Implement multiplication
    return product

def divide(num1, num2):
    division = num1 // num2  # Implement division with zero division check
    return division

def fizz_buzz(number):
    # Implement FizzBuzz logic
    if number == 3:
        return "Fizz"
    elif number == 5:
        return "Buzz"
    elif number == 15:
        return "FizzBuzz"
    else:
        return number

def fibonacci(n):
    fibo = [1, 2]# Implement Fibonacci sequence logic
    count = 1
    if n == 0 and n < 0:
        return 1
    if n == 1:
        return 1
    else:
        for i in range(2, n):
            
            return fibo
        
print(fibonacci(5))
        
def triangle(n):
    pass  # Implement triangle generation logic

def return_list_stats(numbers):
    """Given the list 'numbers', use the relevant functions to return a
        dictionary of statics for the list. This dictionary must have
        the following keys:
            unique_numbers : a set containing unique numbers from the list 'numbers',
            max : largest number in the list 'numbers',
            min : smallest number in the list 'numbers',
            average : average of the numbers in the list 'numbers',
            even_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            odd_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            even_numbers : a tuple of all the even numbers in the list
                'numbers',
            odd_numbers : a tuple of all the odd numbers in the list 
                'numbers',
            number_of_even_numbers : the total number of even numbers in the 
                list 'numbers',
            number_of_odd_numbers : the total number of even numbers in the list
                 'numbers'
    """
    stats_list = {"unique_numbers": set(numbers), 
                  "max": max(numbers),
                  "min": min(numbers),
                  "avarage": sum(numbers)/len(numbers),
                #   "even_pairs":,
                #   "odd_pairs":,
                  "even_numbers":(i for i in numbers if i % 2 == 0),
                  "odd_nuumbers": (i for i in numbers if i % 2 != 0),
                  "number_of_even_numbers": (len(i) for i in numbers if i % 2 == 0)}

# TODO: (Bonus) Implement the pascal_triangle function below
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """
    pass