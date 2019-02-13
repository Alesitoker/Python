def binarioADecimal(num):
    result = 0;
    for i in str(num):
        result = result * 2 + int(i);
    print(result)

binarioADecimal(1011001)