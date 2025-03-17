LIMIT = 100

def digit_sum(num):
    s_num = str(num)
    sum = 0
    for l in s_num :
        sum += int(l)
    return sum

max_digit_sum = 0
for a in range(0, LIMIT+1):
    for b in range(0, LIMIT+1):
        sum = digit_sum(a**b)
        if sum > max_digit_sum :
            max_digit_sum = sum
            # print (sum)

print(str(max_digit_sum))
