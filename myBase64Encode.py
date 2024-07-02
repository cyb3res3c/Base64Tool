def decimalToBinary(number):
    # 0xFF 确保取低八位
    return format(number & 0xFF, '08b')


def splitStringByLength(string, length):
    count = 0
    tempString = ""
    resultList = []
    for char in string:
        tempString += char
        count += 1
        if count == length:
            count = 0
            tempString = "00" + tempString
            resultList.append(tempString)
            tempString = ""

    stringLength = len(tempString)
    count = 0

    if stringLength != 0:
        tempString = "00" + tempString
        stringLength = len(tempString)

        if stringLength < 8:
            for i in range(8 - stringLength):
                tempString += '0'
                count += 1

        resultList.append(tempString)
    flag = int(count / 2)
    return flag, resultList


def base64AlphabetGenerator():
    bs64Alphabet = {}

    originUpperChar = 'A'
    originLowerChar = 'a'
    originNumberChar = '0'

    for i in range(0, 62):
        if i < 26:
            bs64Alphabet[i] = chr(ord(originUpperChar) + i)
        elif i < 52:
            bs64Alphabet[i] = chr(ord(originLowerChar) + i - 26)
        elif i < 62:
            bs64Alphabet[i] = chr(ord(originNumberChar) + i - 52)

    bs64Alphabet[62] = '+'
    bs64Alphabet[63] = '/'
    return bs64Alphabet


def myBase64Encode(decodeString):
    binaryList = []
    binaryString = ""
    encodeInfo = ""

    base64Alphabet = base64AlphabetGenerator()
    for char in decodeString:
        binaryList.append(decimalToBinary(ord(char)))

    for element in binaryList:
        binaryString += element

    flag, handleList = splitStringByLength(binaryString, 6)

    for i in handleList:
        index = int(i, 2)
        encodeInfo += base64Alphabet[index]
    for i in range(flag):
        encodeInfo += '='

    return encodeInfo
