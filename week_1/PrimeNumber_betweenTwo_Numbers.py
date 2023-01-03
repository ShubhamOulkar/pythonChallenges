left = int(input("left: "))
right = int(input("right: "))

# prime numbers in the range
prime_number = []
for i in range(left, right +1):
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
    if c  == 1:
        prime_number.append(i)
#print(prime_number)

if len(prime_number) == 1:
    print([-1, -1])
else:
    # subtract each prime number in a list and store result in dictionary
    key = []
    sub = []
    for k in range(len(prime_number) - 1):
        key.append([prime_number[k], prime_number[k + 1]])
        sub.append(prime_number[k + 1] - prime_number[k])
    #print(key)
    # find minimum sub value and its key
    minimum_prime = []
    minimum_sub = min(sub)
    for p in range(len(sub)):
        if sub[p] <= minimum_sub:
            minimum_prime.append(key[p])
    print(minimum_prime[0])


#
# # subtract each prime number in a list and store result in dictionary
# key = []
# sub = []
# for k in range(len(prime_number)-1):
#     key.append(f"{prime_number[k + 1]} - {prime_number[k]}")
#     sub.append(prime_number[k + 1] - prime_number[k])
# # find minimum sub value and its key
# minimum_prime = []
# minimum_sub = min(sub)
# for p in range(len(sub)):
#     if  sub[p] <= minimum_sub:
#         minimum_prime.append(key[p])
#
# print(minimum_prime)
#
#
#
