def deSegundos(segundos):
    horas = 0
    minutos = 0
    seg = 0
    time = []

    horas = segundos / 3600
    minutos = (segundos % 3600) / 60
    seg = (segundos %3600) %60

    time.append(int(horas))
    time.append(int(minutos))
    time.append(int(seg))
    return time

segundos = int(input("Introduce numero de segundos:"))
print(deSegundos(segundos))
