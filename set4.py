##1
def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = "cinema"
word2 = "iceman"
result = are_anagrams(word1, word2)
print(result)
