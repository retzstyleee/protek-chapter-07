# data = open("Praktikum7.3.txt","r")
# sum = 0
# for x in data:
#     sum += int(x)
# print(sum)

data = open("Praktikum7.3.txt","r")
sum = 0
for x in data:
    try:
        sum += int(x)
    except:
        pass
print(sum)