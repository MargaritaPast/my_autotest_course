# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

from pathlib import Path
import re


path = Path("test_file/task1_data.txt")
answer_fl = open("test_file/task1_answer.txt", "w+", encoding='utf-8')

fl = open(path, mode='r', encoding='utf-8')
ln = fl.readlines()
for one_line in ln:
    new_fl = re.sub("[0|1|2|3|4|5|6|7|8|9]", "", one_line).strip()
    answer_fl.write(new_fl)
    if one_line != ln[-1]:
        answer_fl.write("\n")


answer_fl.close()




#print(*fl)
#for one_line in fl.readlines():
    #print(one_line, end='')

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
