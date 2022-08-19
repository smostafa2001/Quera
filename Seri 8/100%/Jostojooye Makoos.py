from string import punctuation as pc
sentence=input()
word=input()
sentence=sentence.lower()
for i in pc:
    if i in sentence:sentence=sentence.replace(i,' ')
numbers=['0','1','2','3','4','5','6','7','8','9']
for i in numbers:
    if i in sentence:sentence=sentence.replace(i,' ')
sentence=sentence.split()
word=word.lower()
word=word.strip()
tekrari1=sentence.count(word)
tekrari2=sentence.count(word[::-1])
tekrari3=tekrari1+tekrari2
print(tekrari3)