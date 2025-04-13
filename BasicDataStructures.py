# Python code​​​​​​‌‌​‌​​‌​​​​‌‌‌​‌​‌‌​​‌​‌​ below


def encodeString(stringVal):
    # Your code goes here.
    prev_char = stringVal[0]
    prev_count = 1
    result = []
    for item in stringVal[1:]:
        if item == prev_char:
            prev_count += 1
        else:
            result.append((prev_char, prev_count))
            prev_char = item
            prev_count = 1
    result.append((prev_char, prev_count))
    return result


def decodeString(encodedList):
    result = ''
    for item in encodedList:
        result += item[0] * item[1]
    return result
