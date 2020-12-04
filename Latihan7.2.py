text = open("Latihan7.2.txt","a")
while True:
    print("Masukan text untuk ditambahkan : ",end="")
    text.write(input(""))
    text.close
    kode = input("Ingin menambahkan lagi ? (y)")
    if kode == "y":
        continue
    else:
        break
text = open("Latihan7.2.txt","r")
print("Isi : \n",text.read())