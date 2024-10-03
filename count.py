'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
'''
def count_occurrences(elements, value):
    return elements.count(value)

# Input
input_data = input("Enter the list elements: ")  # First line of input for the list
elements = list(map(int, input_data.split()))  # Convert input string to a list of integers
value_to_count = int(input("Enter the value to count: "))  # Second line of input for the value to count

# Count occurrences
count = count_occurrences(elements, value_to_count)

# Output the result
print(count)

