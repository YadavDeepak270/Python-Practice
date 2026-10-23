2. #Given A and B, the task is to find the number of possible values
# that X can take such that the given modular equation (A mod X) = B holds good.
# Here, X is also called a solution of the modular equation.

# Input : A = 26, B = 2
# Output : 6
# Explanation
# X can be equal to any of {3, 4, 6, 8,
# 12, 24} as A modulus any of these values
# equals 2 i. e., (26 mod 3) = (26 mod 4)
# = (26 mod 6) = (26 mod 8) = Output: 2

# Input : 21 5
# Output : 2
# Explanation
# X can be equal to any of {8, 16} as A modulus
# any of these values equals 5 i.e. (21 mod
# 8) = (21 mod 16) = 5
# Hint :
'''def count_possible_values(A, B):
    count=0
    for X in range(1,ArithmeticError+1):
        if A%X==B:
            count+=1
    return count
A1,B1=26,2
A2,B2=21,5
output1=count_possible_values(A1,B1)
output2=count_possible_values(A2,B2)   
print(f"Input: A = {A1}, B = {B1}, Output: {output1}") 
print(f"Input:A={A2},B={B2},Output:{output2}") '''
num1=int(input("Enter the value of A: "))
num2=int(input("Enter the value of B: "))
count=0
for i in range(1,num1+1):
    if num1%i==num2:
       count+=1
print(f"is the:{count}")
      
     
