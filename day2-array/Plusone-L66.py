digits = [9]
res = ''
for i in range(len(digits)):
    res += str(digits[i])
    
    
result = [int(x) for x in str(int(res)+1)]
print(result)