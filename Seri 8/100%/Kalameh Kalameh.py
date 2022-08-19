word=input()
vowels='aeiou'
vowel_counter=0
for letter in word:
    for vowel in vowels:
        if letter==vowel:vowel_counter+=1
print(2**vowel_counter)