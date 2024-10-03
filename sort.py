'''
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''
def sort_and_print(numbers):
    # Sort the list
    sorted_numbers = sorted(numbers)
    # Print the sorted list
    print(" ".join(map(str, sorted_numbers)))

# Input
input_data = list(map(int, input("Enter the numbers: ").split()))

# Call the function to sort and print the numbers
sort_and_print(input_data)

