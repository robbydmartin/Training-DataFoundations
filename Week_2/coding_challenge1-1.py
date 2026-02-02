
N = input()
K = int(input())
M = int(input())

# num = 1

# while K != 0:

#     # Loop through N to multiply each digit
#     for digit in str(N):
#         num *= int(digit)

#     # Decrement the value of K for the 
#     K-= 1

#     # Check if K has reached 0 and break the while loop if so.
#     if K == 0:
#         break

#     N = num % M

#     # Check if N contains only one digit and break the while loop if so
#     if N < 10:
#         break

#     # Decrement the value of K.
#     K -= 1

# print(N)

#### WORKING SOLUTION

# Loop K times
for i in range(K):
    # Set variable num to 1 at each iteration
    num = 1
    # Loop through each digit of N, multiplying each digit
    for x in str(N):
        num *= int(x)
    # Assign N to num mod M
    N = num % M


print(N)