# Write a function is_one_away (word1, word2) that takes two words word1 and word2 as arguments and
# returns True if the words have the same length and differ by exactly 1 character, and False otherwise.
def is_one_away(word1, word2):
    count = 0
    for c in range(len(word1)):
        if word1[c] != word2[c]:
            count += 1
    return count == 1


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))
