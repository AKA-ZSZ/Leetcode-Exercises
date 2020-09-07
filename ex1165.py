def calculateTime(keyboard, word):
    index = 0
    time = 0
    for chr in word:
        time += abs(keyboard.index(chr) - index)
        index = keyboard.index(chr)
    return time

# testcases
# keyboard = "abcdefghijklmnopqrstuvwxyz"
# keyboard2 = "pqrstuvwxyzabcdefghijklmno"
# word = "cba"
# word2="leetcode"
# print(calculateTime(keyboard, word));
# print(calculateTime(keyboard2, word2));
