ignore = ["a", "an", "the", "A", "An", "The"]
words = input("Input : ").split()
filteredWords = []
i = 0
while i < len(words):
    if words[i] not in ignore:
        filteredWords.append(words[i])
    i += 1
print(filteredWords)