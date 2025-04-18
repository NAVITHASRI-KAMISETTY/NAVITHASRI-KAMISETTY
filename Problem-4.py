input_list = input().strip()
if input_list.startswith('[') and input_list.endswith(']'):
    input_list = input_list[1:-1]
input_list = [int(num.strip()) for num in input_list.split(",")]
count_dict = {}
for i in range(1, 10):
    count = 0
    for num in input_list:
        if num % i == 0:  
            count += 1  
    count_dict[i] = count  
print(count_dict)
