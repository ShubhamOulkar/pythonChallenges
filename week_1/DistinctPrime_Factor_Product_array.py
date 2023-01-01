
num = input("Enter array: ")
nums = num.strip('][').split(',')
print(nums)
big_integer = []
# product of integers in a list
product = 1
for p in range(0, len(nums)):
    big_integer.append(int(nums[p]))
    product *= int(nums[p])
print(product)
# Find factors of product
big = max(big_integer)
factors = []
for f in range(2,big+1): # nums[len(nums)
    if product % f == 0:
        factors.append(f)
print(factors)
# find prime factors
prime_factors = []
for pf in factors:
    c = 0
    for fp in range(1,pf):
        if pf % fp == 0:
            c += 1
    if c == 1:
        prime_factors.append(pf)
print(prime_factors)
# output number of prime factor
print(len(prime_factors))
