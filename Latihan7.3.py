array = []
try:
    sum = 0
    while True:
        bil_raw = input("Bilangan : ")
        bil = int(bil_raw)
        array.append(bil)
        conf = input("Lanjut ? (y)")
        if conf != "y":
            break
    for a in array:
        sum += a
    print(sum / len(array))
except :
    print("Maaf bilangan Tidak Valid")