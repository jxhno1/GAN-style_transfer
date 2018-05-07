# according to test its wrong below
def add_binary(a, b):
    c = [0]*(len(a)+1)
    carry = 0
    for i in range(len(a)):
        c[i] = (a[i] + b[i] + carry) // 2
        carry = (a[i] + b[i] + carry) % 2
        c[i+1] = carry
    return c

#here a right one below
def addBinary(a, b):
    lengthA = len(a)
    lengthB = len(b)
    lendiff = lengthA - lengthB
    diststring = ''
    for i in range(abs(lendiff)):
        diststring += '0'
    if lendiff > 0:
        b = diststring + b
    else:
        a = diststring + a
    i = max(lengthA, lengthB) - 1
    resultString = ''
    curCarry = 0
    while i >= 0:
        curPos = (int(a[i]) + int(b[i]) + curCarry) % 2
        resultString = str(curPos) + resultString
        if i == 0:
            if (int(a[i]) + int(b[i]) + curCarry) >= 2:
                return '1' + resultString
            else:
                return resultString
        else:
            if (int(a[i]) + int(b[i]) + curCarry) >= 2:
                curCarry = 1
            else:
                curCarry = 0
        i -= 1
if __name__ == '__main__':
    a = '110'
    b = '101'
    print(addBinary(a, b))

