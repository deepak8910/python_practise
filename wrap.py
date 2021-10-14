inputx = "Following up from last week in case my note got lost in your inbox President Joe Biden would be the third United States President that Prime Minister Modi would be engaging"
length = 30

def wrap(inputx, length):
    i = 0
    inputx = list(inputx) 
    while i < len(inputx):
        i = i + length
        if i < len(inputx):
            if inputx[i] == ' ':
                inputx[i] = '\n'
            else:
                for j in range(i,0,-1):
                    if inputx[j] == ' ':
                        inputx[i-j] = '\n'
                        break
    return ''.join(inputx)

print(wrap(inputx,length))