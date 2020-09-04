import re


# remove vowels in a string
def removeVowels(s):
    # 1st method
    # vowels = ["a", "e", "i", "o", "u"]
    # str = ""
    # for chr in s:
    #     if chr not in vowels:
    #         str = str + chr
    #
    # return str

    # 2nd method- use regular expression operations module
    str = re.sub("[aeiou]", "", s)
    return str


# testcases
if __name__ == "__main__":
    str = "aeiour"
    print(removeVowels(str))

    # str2 = "leetcodeisacommunity"
    # print(removeVowels(str2))
