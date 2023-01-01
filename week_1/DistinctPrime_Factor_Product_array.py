
num = input("Enter array: ")
nums = num.strip('][').split(',')
print(nums)

# product of integers in a list
product = 1
for p in range(0, len(nums)):
    product *= int(nums[p])
print(product)
# Find factors of product
factors = []
for f in range(2,10):
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

# output number of prime factor
print(len(prime_factors))
