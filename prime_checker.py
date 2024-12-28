"""Program to check if a number is prime."""
import math

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        if n % i == 0:
            return False
    return True

def find_primes_up_to(limit: int) -> list[int]:
    """Find all prime numbers up to a limit."""
    return [num for num in range(2, limit + 1) if is_prime(num)]

def list_primes_in_range(start: int, end: int) -> list[int]:
    """List all prime numbers in a range."""
    return [num for num in range(start, end + 1) if is_prime(num)]

def main()-> None:
    '''Main function.'''
    try:
        number = int(input("Enter a number to check if it's prime: "))
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

    try:
        divisor = int(input("Enter a divisor for calculation: "))
        result = 100 / divisor
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
