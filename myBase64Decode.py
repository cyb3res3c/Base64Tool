def splitStringByLength(string, length):
    handleList = []
    tempString = ""
    count = 0

    for char in string:
        tempString += char
        count += 1
        if count == length:
            handleList.append(tempString)
            count = 0
            tempString = ""
    if len(tempString) != 0:
        handleList.append(tempString)
    return handleList


def decimalToBinary(number):
    return format(number & 0xFF, '08b')


def finKeyByValue(keyValue, bs4alphabent):
    for key, value in bs4alphabent.items():
        if value == keyValue:
            return key
    return -1


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


def myBase64Decode(encodeString):
    keyList = []
    binaryList = []
    decimalList = []
    binaryString = ""
    decodeString = ""

    count = encodeString.count('=')
    if count != 0:
        encodeString = encodeString.replace('=', '')
    base64Alphabet = base64AlphabetGenerator()

    for char in encodeString:
        keyList.append(finKeyByValue(char, base64Alphabet))

    for number in keyList:
        binaryList.append(decimalToBinary(number))

    binaryListLength = len(binaryList)

    for index in range(binaryListLength):
        binaryList[index] = binaryList[index][2:]

    if count != 0:
        for i in range(count * 2):
            binaryList[binaryListLength - 1] = binaryList[binaryListLength - 1][: -1]

    for element in binaryList:
        binaryString += element

    originBinaryList = splitStringByLength(binaryString, 8)

    for originBinaryString in originBinaryList:
        decimalList.append(int(originBinaryString, 2))

    for asciiNumber in decimalList:
        decodeString += chr(asciiNumber)

    return decodeString
