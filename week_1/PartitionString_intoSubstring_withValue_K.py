number_string = input("Number string: ")
value_k = int(input("value of k: "))
sub_string = []
loop = len((str(value_k)))

print(number_string)

for ff in range(0, loop):
    condition = ff + 1
    # padding zeros make number string multiple of number of digit values of K
    if condition == 2 and len(number_string) % 2 != 0:
        number_string += "0"
    elif condition == 3 and len(number_string) % 3 == 1:
        number_string += "00"
    elif condition and len(number_string) % 3 == 2:
        number_string += "0"

    is_ok = True
    j = 0
    while is_ok:
        strin = ""
        for i in range(j, condition + j):
            strin += number_string[i]
            j += 1
        sub_string.append(strin)
        if j == len(number_string):
            is_ok = False

# The value of each substring must be less then value_k
ans = []
for s in sub_string:
    for l in range(loop):
        l += 1
        if len(s) == l:
            if int(s) < value_k:
                ans.append(s)

# Each digit must be part of exactly one substring
print(ans[: :-1])




