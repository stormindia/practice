# Given an array of N positive integers, print k largest elements from the array.  The output elements should be printed in decreasing order.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
#The first line of each test case is N and k, N is the size of array and K is the largest elements to be returned.
#The second line of each test case contains N input C[i].
#
# Output:
# Print the k largest element in descending order.
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 100
# K ≤ N
# 1 ≤ C[i] ≤ 1000
#
# Example:
# Input:
# 2
# 5 2
# 12 5 787 1 23
# 7 3
# 1 23 12 9 30 2 50
#
# Output:
# 787 23
# 50 30 23
#
# Explanation:
# Testcase 1: 1st largest element in the array is 787 and second largest is 23.
# Testcase 2: 3 Largest element in the array are 50, 30 and 23.

number_of_test_cases = int(input('number_of_test_cases '))
output_arr = []

for i in range(number_of_test_cases):
    take_input = input('array size and k elements ')
    arr_size = int(take_input[0])
    k_elements = int(take_input[2])
    curr_output = []

    arr = list(map(int, input().split()))
    #print(arr)

    MIN = 9999
    MIN_POS = 0
    for i in range(len(arr)):
        if(len(curr_output) < k_elements):
            curr_output.append(arr[i])
            if(MIN > arr[i]):
                MIN = arr[i]
                MIN_POS = i
        else:
            if(arr[i] > MIN):
                curr_output[MIN_POS] = arr[i]
                MIN = 9999
                for j in range(k_elements):
                    if(curr_output[j] < MIN):
                        MIN = curr_output[j]
                        MIN_POS = j

    #curr_output = curr_output
    output_arr.append(sorted(curr_output, reverse=True))

print(output_arr)
