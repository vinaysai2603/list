'''
Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
'''
def sum_of_array(arr):
    return sum(arr)

# Input
input_data = list(map(int, input("Enter the integers: ").split()))
n = input_data[0]  # The first integer represents n
array_elements = input_data[1:n+1]  # The next n integers are the elements of the array

# Calculate the sum
total_sum = sum_of_array(array_elements)

# Output the sum
print(total_sum)

