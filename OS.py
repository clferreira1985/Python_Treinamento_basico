import os

# saber o caminho
# esse caminho que estou "c:\\Users\\Clfer\\OneDrive\\Cursos\\Asimov\\1. Python Starter\\OS\\pasta"

os.getcwd()

# saber os diretorios da pasta
os.listdir()

# conhecer os arquivos que estão em outras pastas
os.listdir("\\Users\\Clfer\\OneDrive\\Cursos\\Asimov\\1. Python Starter")

# Alterar a pasta onde você está alocado
atual_dir = os.getcwd()
os.chdir("\\Users\\Clfer\\OneDrive\\Cursos\\Asimov\\1. Python Starter")
print(os.getcwd())
os.chdir(atual_dir)

# Criar pasta
os.mkdir("Pasta2")

# Renomear (arquivo atual, para qual arquivo estou colocando)
os.rename("teste.txt", "teste2.txt")

# remove arquivos
os.remove("teste.csv")

# remove pastas

os.rmdir("Pasta2")

#
os.system

# Tem as mesmas funcionalidade, sendo a segunda melhor
os.path.join(os.getcwd(), "pasta")
os.getcwd() + "/pasta"

# retorna a ultima pasta desse caminho
os.path.basename(os.getcwd())

# retorna a ultima pasta desse caminho fazendo um split do caminho
os.getcwd().split("\\")[-1]

# retorna tudo antes da pasta
os.path.dirname(os.getcwd())
