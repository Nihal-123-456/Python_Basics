def add(nums):
    nums_list = list(map(float, nums.split()))
    result = sum(nums_list)
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(nums):
    nums_list = list(map(float, nums.split()))
    result = 1
    for n in nums_list:
        result = result*n
    return result

def divide(num1, num2):
    if num2 == 0:
        return 'You cannot divide a number by zero'
    result = num1/num2
    return result