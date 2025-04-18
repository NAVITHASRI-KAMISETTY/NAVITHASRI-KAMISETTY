a = int(input())
i = 1
count = 0
if a % 2 == 0:
    limit = a - 1
else:
    limit = a
while count < limit:
    print(i, end="")
    count += 1
    if count < limit:
        print(",", end="")
    i += 2
