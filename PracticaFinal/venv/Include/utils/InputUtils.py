def inputString(message):
    string = ''

    string = str(input(message))

    return string

def inputNumber(message, errorMsg = ""):
    number = 0

    while True:
        try:
            number = int(input(message))
            break
        except ValueError:
            if errorMsg != "":
                print(errorMsg)

    return number