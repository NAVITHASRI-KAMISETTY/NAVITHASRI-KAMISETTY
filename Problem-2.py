a = int(input())
i = 1
count = 0
while count < a:
    print(i, end="")
    count += 1
    if count < a:
        print(",", end="")
    i += 2
