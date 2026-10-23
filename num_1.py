#1. Python Program for Check if all digits of a number divide it

# Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Input : 130
# Output : No
'''num1 = 128
num2 = 130

for current_num in [num1, num2]:
    num_str = str(current_num)
    is_divisible = True
    
    for i in num_str:
        digit = int(i)
        if digit == 0 or current_num % digit != 0:
            is_divisible = False
            break
            
    if is_divisible:
        print(f"Input: {current_num}, Output: Yes")
    else:
        print(f"Input: {current_num}, Output: No")'''


# Solution -
def check_divisibility(num):
    # Convert the number to a string to iterate through its digits
    num_str = str(num)

    # Iterate through each digit and check if it divides the number
    for digit_str in num_str:
        digit = int(digit_str)
        if digit == 0 or num % digit != 0:
            return "No"

    # If all digits divide the number, return "Yes"
    return "Yes"

# Test cases
num1 = 128
num2 = 130

output1 = check_divisibility(num1)
output2 = check_divisibility(num2)

print(f"Input: {num1}, Output: {output1}")
print(f"Input: {num2}, Output: {output2}")
