num = int(input(' '))
i = num

while i > 1:
    num *= (i-1)
    i += -1

print (num)