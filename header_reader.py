import os

path_save = 'D:\\WS20-21\\Projekt\\Emails'
file_save_res = open("results_file.txt", "w+")

for file in os.listdir(path_save):
    path_load = os.path.join(path_save, file, 'message.txt')
    with open(path_load, 'r', errors='ignore') as f:
        for line in f.readlines():
            if line.find('From') != -1:
                file_save_res.write(f"From: {line}\n")
            if line.find('To') != -1:
                file_save_res.write(f"To: {line}\n")
            if line.find('CC') != -1:
                file_save_res.write(f"CC: {line}\n")
            if line.find('Subject') != -1:
                file_save_res.write(f"Subject: {line}\n")
            if line.find('Date') != -1:
                file_save_res.write(f"Date: {line}\n")
            else:
                continue

file_save_res.close()