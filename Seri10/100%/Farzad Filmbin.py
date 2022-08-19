n=int(input())
films=[]
for i in range(n):
    films.append(input())
films=[film.title() for film in films]
for film in films:
    print(film)
