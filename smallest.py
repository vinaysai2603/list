'''
Write a Python Program to find the smallest number in a list
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
1
'''
def find_smallest_number(numbers):
    return min(numbers)

# Input
size = int(input("Enter the size of the list: "))  # First input for the size of the list
numbers = []

# Collecting the numbers
for _ in range(size):
    num = int(input())
    numbers.append(num)

# Find the smallest number
smallest_number = find_smallest_number(numbers)

# Output the smallest number
print(smallest_number)

