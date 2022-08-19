word = input()
print(word)
for i in range(1, len(word)):print(f"{word[i] * i}{word[i:]}")