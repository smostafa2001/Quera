import string
paragraph=input()
for character in string.whitespace:
    paragraph=paragraph.replace(character,' ')
for character in string.punctuation:
    paragraph=paragraph.replace(character, '')
vowels = ["a", "e", "i", "o", "u", "y"]
issues = []

l_paragraph = paragraph.split()

for word in l_paragraph:
    if word.isupper():
        continue
    elif len(word) < 5:
        continue
    elif len(word) == 5:
        flag = False
        for letter in word:
            if (letter in vowels):
                flag = True
        if flag == True:
            continue
        else:
            issues.append(word)
            continue
    else:
        counter = 0
        for letter in word:
            if letter in vowels:
                counter += 1
        if counter >= (len(word)//3) or counter >= (len(word)//4):
            continue
        else:
            issues.append(word)
            continue
issues=str(issues)
for character in string.punctuation:
    issues=issues.replace(character,'')
print(issues)
