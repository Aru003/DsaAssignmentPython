base_62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# 1. For our first problem, write a function that converts a given base-62 string
#    into an integer. Only a single string will be provided, and it will be up to
#    11 characters in length.


def to_base_10(videoId):
    reverse_string = videoId[::-1]
    totalValue = 0
    for index, x in enumerate(reverse_string):
        mapValue = base_62.index(x)
        decimalValue = (mapValue * (62 ** index))
        totalValue += decimalValue

    return totalValue


# 2. Write a function that does the opposite of the previous one. That is, it
#    encodes a integer video key as a base-62 string.

def to_base_62(number):
    base62_value = ""
    while number > 0:
        modValue = number % 62
        base62_value += base_62[modValue]
        number = number // 62
    return base62_value[::-1]




videoId = "LpuPe81bc2w"
#Base62 to Base10
base10_value = to_base_10(videoId)
print(base10_value)

#Base10 to Base62
base62_value = to_base_62(base10_value)
print(base62_value)
