number_string = input("Enter number string:")
val_k = int(input("Enter value of k: "))
ok = len(number_string) // len(str(val_k))
#remaining_digits = len(number_string) % len(str(val_k))
#step = len(number_string) - remaining_digits + 1
sub_string = []
for i in range(ok):
    a = 0 + (i*len(str(val_k)))
    b = len(str(val_k)) + (i*len(str(val_k)))
    sub_string.append(number_string[a:b])

# for j in range(remaining_digits):
#     a = step + j
#     sub_string.append(number_string[a])

print(sub_string)

ans0 = []
ans1 = []
for sub in sub_string:
    if int(sub) <= val_k:
        ans0.append(sub)
    else:
        ans1.append(sub)

print(ans0)
print(ans1)
check = "".join(ans0)
if check == number_string:
    print(len(ans0))
else:
    for p in ans1:
        for q in range(len(p)):
            if int(p[q])<= val_k:
                ans0.append(p[q])
    check1 = "".join(ans0)
    if check1 == number_string:
        print(len(ans0))
    else:
        print("-1")


# 21372772
# 17
