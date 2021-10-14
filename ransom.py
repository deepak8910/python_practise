def find_str(mag,rans):
    i = j = 0
    d = {}
    while i<len(mag) and j<len(rans):
        if mag[i] not in d.keys():
            d[mag[i]]=1
        else:
            d[mag[i]] += 1
        if rans[j] in d.keys():
            if d[rans[j]] > 0:
                d[rans[j]] -= 1
                j += 1
        i += 1
    print(i,j)
    if j == len(rans):
        return True
    if i == len(mag):
        return False

mag = "programming interviews are weird"
rans = "no scheme"

print(find_str(mag,rans))
