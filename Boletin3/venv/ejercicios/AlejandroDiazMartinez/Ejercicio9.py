def es_bisiesto(year):
    if year%4 == 0 and year%100 != 0:
        return True
    return False


print("Introduce un año:")
year = int(input())

if es_bisiesto(year):
    print("Es bisiesto")
else:
    print("No es bisiesto")