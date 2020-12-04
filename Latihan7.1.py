directory = input("Masukan Direktori File : ")
try:
    text = open(directory,"r")
    print("Isi file dari direktori {} adalah : \n {}".format(directory,text.read()))
except :
    print("Maaf, direktori tidak valid")