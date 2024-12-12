# """
# работа с файлами
# """
# #создаем файл с расширением .doc или .txt и даем ему псевданим
# with open("text.doc","w+",encoding="UTF-8") as NewFile:
#     NewFile.write("АХАХАХАХАХАХХА \n")
#
# with open("text.doc","a+",encoding="UTF-8") as NewFile:
#     for i in range(10):
#         NewFile.writelines(["aasdasd","\n","asdasdasd","\n","asdasddas"])
# def get_sum(a,b):
#     if a > b:
#         a,b = b,a
#     if b >= 0:
#         return sum(range(a,b+1))
#     elif a < 0 and b < 0:
#         return sum(range(a,b+1))
#     else:
#         return sum(range(b,a+1))
def addBinary(a: str, b: str) -> str:
    return bin(int(a))+bin(int(b))

print(addBinary("11","1"))