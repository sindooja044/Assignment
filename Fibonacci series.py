def generate_fibonacci(n):
    if n <= 0:
        return "The number of terms must be a positive integer."
    
    fibonacci_sequence = []
    
    # First two terms of the Fibonacci sequence
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

def main():
    try:
        n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
        
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            sequence = generate_fibonacci(n)
            print(f"Fibonacci sequence with {n} terms: {sequence}")
    
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
