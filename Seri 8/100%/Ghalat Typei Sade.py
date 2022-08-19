paragraph = input().strip()
pc= "'!#$%^\()*+,-./:;<=>?@[\]^_'{|}-'"
for word in paragraph:
    if word in pc:paragraph=paragraph.replace(word,' ')
notVowles='bcdfghjklmnpqrstvwxyz'
listOfParagraph=paragraph.split()
issues=[]
for word in listOfParagraph:
    if len(word)>=5:
        for j in range(len(word)-4):
            first=word[j]
            second=word[j+1]
            third=word[j+2]
            forth=word[j+3]
            fifth=word[j+4]
            if (first in notVowles) and (second in notVowles) and (third in notVowles) and (forth in notVowles) and (fifth in notVowles) :
                issues.append(word)
                break
for issue in issues:print(issue,end=' ')