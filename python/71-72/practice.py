# all_files =[]
# while True:
#     file_name = input("Введите имя файла")
#     if file_name == "quit":
#         break
#     all_files.append(file_name)
#
#
#
#     with open("resalt.txt","w",encoding="utf-8") as res:
#         for file in all_files:
#             with open(file,"r",encoding="utf-8") as cur_file:
#                 res.writelines(cur_file.readlines())


# all_files =[]
# while True:
#     file_name = input("Введите имя файла")
#     if file_name == "quit":
#         break
#     all_files.append(file_name)
#
#
#     common_set = set()
#     with open("resalt2.txt","w+",encoding="utf-8") as res:
#         for file in all_files:
#             with open(file,"r",encoding="utf-8") as cur_file:
#                 common_set = set(cur_file.read())
#                 for i in cur_file.read():
#                     common_set.intersection_update(i)
#                 print(common_set)
#                 res.write("".join(common_set))


# all_files =[]
# while True:
#     file_name = input("Введите имя файла")
#     if file_name == "quit":
#         break
#     all_files.append(file_name)
#
#     for file in all_files:
#         with open(file,"r",encoding="utf-8") as cur_file:
#

# with open("stat.txt","r",encoding="utf-8") as stat:
#     out_put = stat.read().lower()
#     # sogl = {"б","в","г","д","ж","з","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш","щ","ъ","ь"}
#     # glasn = {"a","е","ё","и","й","о","у","ы","э","ю","я"}
#     res = []
#     for i in out_put:
#         if i.isdecimal():
#             res.append(int(i))
#     print(sum(res))
pizza = int(input("Введите диаметр пиццы"))
area = 3.14 * (pizza/2)**2
with open("pizza.txt","a+",encoding="utf-8") as file:
    file.write(f"{area}" "\n")