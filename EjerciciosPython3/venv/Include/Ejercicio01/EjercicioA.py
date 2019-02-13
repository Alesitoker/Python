def aSegudos(horas, minutos, segundos):
    return (horas * 3600) + (minutos * 60) + segundos



horas = int(input("Introduce numero de horas:"))
minutos = int(input("Introduce numero de minutos:"))
segundos = int(input("Introduce numero de segundos:"))

print(aSegudos(horas, minutos, segundos))