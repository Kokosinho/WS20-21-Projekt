import os

path_save = 'D:\WS20-21\Projekt\.MSG\Projekt\Feuerwehr - Ausgang\Posteingang\Text'

for file in os.listdir(path_save):
    path_load = os.path.join(path_save, file, 'message.txt')
    with open(path_load, 'r', errors='ignore') as f:
        for line in f.readlines():
            if  line.find('Subject') != -1:
                print(line)
            else:
                continue
