from pprint import pprint

full_database = []
# let it be composed of lists [number of lines, name of the file, text by lines]

list_of_filenames = ['text3.txt', 'text2.txt', 'text1.txt']

for filename in list_of_filenames:
    with open(filename, 'rt', encoding="utf-8") as file:
        entry_for_database = [0, "", []]
        full_text = file.readlines()
        entry_for_database[0] = len(full_text)
        entry_for_database[1] = filename
        entry_for_database[2] = full_text
        full_database.append(entry_for_database)

full_database.sort()

with open('final_file.txt', 'w', encoding="utf-8") as file:
     for entry_in_database in full_database:
         file.write(f"{entry_in_database[1]}\n")
         file.write(f"{entry_in_database[0]}\n")
         file.writelines(entry_in_database[2])
         file.write("\n") # for readability of the file






