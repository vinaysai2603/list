'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
'''
def print_reverse(numbers):
    # Print the numbers in reverse order
    print(" ".join(map(str, reversed(numbers))))

# Input
input_data = input("Enter the numbers: ")  # Take input as a single line
numbers = list(map(int, input_data.split()))  # Convert the input into a list of integers

# Call the function to print the numbers in reverse order
print_reverse(numbers)

