def añoHoy(now, names, years):
    results = []
    for i in range(len(years)):
        age = now - years[i]
        results.append(names[i] + " cumplira " + str(age) + " años en " + str(now))
    for i in results:
        print(i)

names = []
years = []

print("Introduce año actual:")
now = int(input())
for i in range(3):
    print("Introduce nombre:")
    names.append(str(input()))
    print("Introduce su año de nacimiento:")
    years.append(int(input()))

añoHoy(now, names, years)