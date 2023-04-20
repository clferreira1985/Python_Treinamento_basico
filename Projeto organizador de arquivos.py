## O pequeno projeto tem a finalidade de pegar todos os arquivos que estiverem dentro de uma pasta, organizar cada um em suas respectivas pastas conforme extensão


# import do pacote
import os

# Pego o caminho que está os arquivos
cwd = os.getcwd()

# Pego todos os arquivos e chamo ele de full_list
full_list = os.listdir(cwd)

# O loop abaixo tem a finalidade de olhar cada arquivo e retirar as pastas e arquivos .py
files_list = [i for i in full_list if os.path.isfile(i) and ".py" not in i]


# Primeiro se cria um loop pegando cada extensão de seu arquivos, depois faço um 'set' para selecionar somente os valores sem está com os valores duplicados e coloco dentro de uma lista

file_type = list(set([i.split(".")[1] for i in files_list]))


# Crio uma pasta para cada extensão de arquivo

for file_ext in file_type:
    os.mkdir(file_ext)

# Pego o caminho de cada arquivo e crio o caminho que ele deverá ir
for file in files_list:
    from_path = os.path.join(cwd, file)
    to_path = os.path.join(cwd, file.split(".")[-1], file)

    os.replace(from_path, to_path)
