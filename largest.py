'''
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
'''
def find_largest_number(numbers):
    return max(numbers)

# Input
size = int(input("Enter the size of the list: "))  # First input for the size of the list
numbers = []

# Collecting the numbers
for _ in range(size):
    num = int(input())
    numbers.append(num)

# Find the largest number
largest_number = find_largest_number(numbers)

# Output the largest number
print(largest_number)

