strs = ['notion','creation']
def lcs(strs):
    res = ''
    for i in range(1,len(strs[0])+1):
        for s in strs:
            if s[-i] != strs[0][-i]:
                return res[::-1]
        res = res + strs[0][-i]
    return res[::-1]
result = lcs(strs)
print(result)