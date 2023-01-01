def countDigits(num: int) :
    g = str(num)
    count = 0
    for i in range(len(g)):
        digit = int(g[i])
        if num % digit == 0:
            count += 1
    print(count)
countDigits(int(input("Enter a number: ")))