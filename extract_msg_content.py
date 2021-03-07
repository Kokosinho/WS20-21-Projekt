import extract_msg
import os

path = 'D:\WS20-21\Projekt\.MSG\Projekt\Feuerwehr - Ausgang\Posteingang\Sent/'
path_save = 'D:\WS20-21\Projekt\.MSG\Projekt\Feuerwehr - Ausgang\Posteingang\Text'

os.makedirs(path_save, exist_ok=True)

for file in os.listdir(path):
    load_path = os.path.join(path, file)
    extract_msg.openMsg(load_path).save(customPath=path_save)

