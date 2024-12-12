# with open("text.txt","w",encoding="utf-8") as my_file:
#     lst = ["ах\n","ох\n","лол\n"]
#     for i in range(2):
#         my_file.writelines(lst)
# with open("text.txt", "r", encoding="utf-8") as my_file:
#     for i in my_file:
#         for j in i:
#             for k in j:
#                 print(k,end="")
# with open("text.txt","r",encoding="utf-8") as file:
#     print(len(file.readlines()))
# with open("text.txt","r",encoding="utf-8") as file:
#     with open("text2.txt", "w", encoding="utf-8") as new_file:
#         for i in file:
#             new_file.write(i[::-1])


rus_eng_translit = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "ch",
    "ц": "z",
    "ч": "tsch",
    "ш": "sch",
    "щ": "schtsch",
    "ъ": "",
    "ы": "y",
    "ь": "'",
    "э": "e",
    "ю": "ju",
    "я": "ja"
}

with open("text.txt","r",encoding="utf-8") as file:
     with open("text2.txt", "r", encoding="utf-8") as black:
         with open("text3.txt", "w", encoding="utf-8") as res:
            lack = set(black.read().split("\n"))
            print(lack)
            all_word = file.read().split("\n")
            print(all_word)
            for word in all_word:
                if word.lower() not in lack:
                    res.write(word+"\n")